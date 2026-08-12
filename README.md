# MMPose 验证分支

这个分支用于验证 OpenMMLab MMPose / RTMPose 是否适合做更专业的剑道姿态估计后端。

## 背景判断

MediaPipe 的优点是轻量、接入快，但在剑道视频里会受护具、竹刀遮挡、侧身动作和快速挥动影响。MMPose 更适合做系统化模型实验，因为它提供更多姿态估计模型、模型配置和推理接口。

MMPose 的价值不只是“换一个预训练模型”，而是后续可以支持：

- 更强的人体 2D 姿态模型
- wholebody 模型
- 手部模型
- 3D 姿态或人体网格方向
- 自定义数据集训练
- 自定义关键点布局，例如竹刀柄和剑尖

参考资料：

- MMPose 官方仓库：https://github.com/open-mmlab/mmpose
- MMPose 文档：https://mmpose.readthedocs.io/en/latest/
- MMPose 推理文档提到 `MMPoseInferencer` 可用于图片和视频推理，并提供 human、body26、wholebody 等模型别名。

## 第一轮目标

第一轮只验证预训练模型，不训练：

- `human`
- `body26`
- `wholebody`

重点观察：

- 肩、肘、腕、髋是否比 MediaPipe 稳
- 手腕是否更少飘到竹刀上
- 穿护具时关键点是否仍能贴近身体结构
- 侧面和 45 度视频是否明显改善

## 建议实现步骤

1. 新建独立实验脚本，不急着接入主流程：

```text
experiments/mmpose_inference_check.py
```

2. 安装 MMPose 依赖时单独记录环境，因为 OpenMMLab 依赖较重，Windows 上可能需要额外处理 PyTorch、MMCV、MMEngine。

3. 先用官方 inferencer 跑单张图片或短视频片段。

4. 输出可视化结果到：

```text
data/output/mmpose_check/
```

5. 如果可视化效果明显优于 MediaPipe，再写 adapter：

```text
src/pose/mmpose_detector.py
```

6. 将 MMPose 输出转换成项目当前 points 字典：

```text
left_shoulder
right_shoulder
left_elbow
right_elbow
left_wrist
right_wrist
left_hip
right_hip
```

## 验证指标

每段视频记录：

- 模型名
- 输入分辨率
- 推理速度
- 是否需要 GPU
- 是否能跑完整视频
- 手腕、肘、肩、髋的稳定性
- 是否能识别穿护具画面
- 是否适合接入当前 Python 项目

## 成功标准

如果 MMPose 预训练模型在护具和竹刀场景中明显优于 MediaPipe，可以继续接入为第二后端。

如果预训练模型仍不够稳，但标注和训练路径清晰，则 MMPose 更适合作为“自定义剑道关键点模型”的研究分支。

## 风险

- 安装和部署复杂度高于 YOLO Pose。
- 推理速度可能较慢。
- Windows 环境可能遇到 PyTorch / MMCV 版本兼容问题。
- 不经过自定义训练，仍可能无法解决护具遮挡和竹刀遮挡。

