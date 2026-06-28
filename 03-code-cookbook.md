# 03 代码与命令 Cookbook

这份文件只保留最值得自己敲一遍的内容。目标不是“收藏很多片段”，而是用最小例子理解关键层次。

## 1. 单 GPU 训练骨架

你先要有一个最小训练循环，后面的分布式训练才有意义。

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

x = torch.randn(1024, 128)
y = torch.randint(0, 10, (1024,))
loader = DataLoader(TensorDataset(x, y), batch_size=32, shuffle=True)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = nn.Sequential(nn.Linear(128, 256), nn.ReLU(), nn.Linear(256, 10)).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

for epoch in range(3):
    for batch_x, batch_y in loader:
        batch_x = batch_x.to(device)
        batch_y = batch_y.to(device)

        optimizer.zero_grad()
        logits = model(batch_x)
        loss = criterion(logits, batch_y)
        loss.backward()
        optimizer.step()

    print(f"epoch={epoch} loss={loss.item():.4f}")
```

你在这一步要学会观察：

- GPU 是否被真正使用
- batch size 对显存和吞吐的影响
- 数据加载是否成了瓶颈

## 2. Horovod 分布式训练骨架

Horovod 的价值在于：在现有训练脚本上做相对少量改动，就能扩展到多卡/多机。

```python
import torch
import horovod.torch as hvd

hvd.init()
torch.cuda.set_device(hvd.local_rank())

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

optimizer = hvd.DistributedOptimizer(
    optimizer,
    named_parameters=model.named_parameters(),
)

hvd.broadcast_parameters(model.state_dict(), root_rank=0)
hvd.broadcast_optimizer_state(optimizer, root_rank=0)

for batch_x, batch_y in train_loader:
    batch_x = batch_x.cuda()
    batch_y = batch_y.cuda()

    optimizer.zero_grad()
    loss = criterion(model(batch_x), batch_y)
    loss.backward()
    optimizer.step()
```

常用启动方式：

```bash
horovodrun -np 4 -H localhost:4 python train.py
```

你在这一步要理解：

- `rank` / `local_rank` 是什么
- 为什么需要 broadcast 初始参数
- 为什么分布式训练的关键问题很快会变成通信问题

## 3. Ray 的两个用法

### 3.1 分布式任务

```python
import ray

ray.init()

@ray.remote
def square(x: int) -> int:
    return x * x

results = ray.get([square.remote(i) for i in range(8)])
print(results)
```

这适合先理解 Ray 的“把函数远程化”的模型。

### 3.2 训练骨架

```python
from ray.train import ScalingConfig
from ray.train.torch import TorchTrainer

def train_loop(config):
    model = create_model()
    model = train.torch.prepare_model(model)
    loader = train.torch.prepare_data_loader(create_loader())

    optimizer = torch.optim.Adam(model.parameters(), lr=config["lr"])
    for _ in range(config["epochs"]):
        for x, y in loader:
            optimizer.zero_grad()
            loss = criterion(model(x), y)
            loss.backward()
            optimizer.step()

trainer = TorchTrainer(
    train_loop_per_worker=train_loop,
    train_loop_config={"lr": 1e-3, "epochs": 3},
    scaling_config=ScalingConfig(num_workers=4, use_gpu=True),
)

result = trainer.fit()
```

Ray 更像一个“分布式计算底座”，不止训练，也适合 agent、数据处理、调度和多阶段工作流。

## 4. TensorFlow Serving 最小部署

如果你学的是“把模型服务起来”，TensorFlow Serving 是很典型的起点。

```bash
docker run -p 8501:8501 \
  --mount type=bind,source=/models/my_model,target=/models/my_model \
  -e MODEL_NAME=my_model \
  tensorflow/serving
```

调用预测接口：

```bash
curl -X POST http://localhost:8501/v1/models/my_model:predict \
  -H "Content-Type: application/json" \
  -d '{"instances": [[1.0, 2.0, 3.0, 4.0]]}'
```

这里你要理解的是“模型服务协议”和“线上接口形态”，不是只记命令。

## 5. TorchServe 最小流程

```bash
torch-model-archiver \
  --model-name my_model \
  --version 1.0 \
  --serialized-file model.pth \
  --handler image_classifier \
  --export-path model_store

torchserve --start --model-store model_store --models my_model=my_model.mar
```

这一步学习重点：

- 打包模型和直接跑 Python 脚本的差别
- 模型服务框架如何管理版本、handler 和部署接口

## 6. MLflow：先把实验记录下来

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("lr", 1e-3)
    mlflow.log_param("batch_size", 32)

    for epoch in range(3):
        loss = train_one_epoch(...)
        mlflow.log_metric("loss", loss, step=epoch)

    mlflow.pytorch.log_model(model, artifact_path="model")
```

你学 MLflow，不是为了“打点”，而是为了以后能回答：

- 这个模型是用什么参数训练的？
- 线上这个版本来自哪次实验？
- 为什么这次效果变差了？

## 7. DVC：把数据和 pipeline 也纳入工程流程

```bash
dvc init
dvc add data/raw
git add data/raw.dvc .gitignore
git commit -m "track raw data with dvc"
```

定义 pipeline 的思路：

```bash
dvc stage add \
  -n train \
  -d train.py \
  -d data/processed \
  -o outputs/model.pth \
  python train.py
```

DVC 的核心不是命令，而是这件事：

**数据、脚本、产物之间的依赖关系终于可追踪了。**

## 8. TensorRT / 推理优化该怎么理解

你不一定一开始就要深挖 TensorRT API，但至少要知道优化路径：

1. 先把模型导出成稳定格式，例如 ONNX
2. 再用推理运行时或编译器做图优化、算子融合、量化、batch 优化
3. 最后测延迟、吞吐和显存占用

最重要的不是“上没上 TensorRT”，而是要养成性能评测习惯。

## 9. 我建议你亲手做的最小实验

1. 跑通单 GPU 训练脚本
2. 用 Horovod 或 PyTorch DDP 扩成多卡
3. 用 MLflow 记录训练参数与 loss
4. 把模型用 TorchServe 或 TF Serving 部署出来
5. 用简单脚本压测延迟和吞吐

如果这五步能串起来，你已经不是在看“AI Infra 介绍”，而是在真正进入 AI Infra 实践。
