# YOLO Pose 验证分支

这个分支用于验证 Ultralytics YOLO Pose 是否比当前 MediaPipe Pose 更适合剑道视频分析，尤其是穿护具、拿竹刀、侧身或 45 度拍摄时的关键点稳定性。

## 背景判断

当前 MediaPipe baseline 已经能完整处理视频帧，但在剑道场景里会遇到明显限制：

- 穿护具后，肩、肘、腕、髋的视觉轮廓和普通人体数据差异很大。
- 竹刀和手臂互相遮挡，手腕点容易漂移。
- 快速挥剑会造成运动模糊，单帧关键点不稳定。
- 背面或强侧面视角下，通用人体模型容易左右混淆。

YOLO Pose 的优势是接入简单、视频推理方便、速度快，并且官方 pose 模型直接输出人体关键点坐标和置信度。它仍然是通用 COCO 人体关键点模型，所以第一阶段目标不是立刻替代 MediaPipe，而是做同视频对比。

参考资料：

- Ultralytics Pose 文档：https://docs.ultralytics.com/tasks/pose
- YOLO Pose 输出包含 `result.keypoints.xy`、`result.keypoints.xyn` 和 `result.keypoints.data`，默认人体模型使用 17 个 COCO 关键点。

## 第一轮目标

先不要训练自定义模型，只验证预训练模型能不能更稳定地识别：

- 正面视频
- 45 度斜前方视频
- 侧面视频
- 背面视频
- 穿护具视频
- 拿竹刀快速挥动视频

## 建议实现步骤

1. 安装依赖：

```powershell
pip install ultralytics
```

2. 新增 YOLO detector，不删除 MediaPipe detector：

```text
src/pose/yolo_detector.py
```

3. 使用预训练 pose 模型做第一轮验证：

```python
from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")
results = model(frame)
```

如果当前 Ultralytics 文档推荐更新型号，也可以按官方最新 pose 模型尝试。

4. 将 YOLO 的 17 个关键点转换为项目当前 points 字典：

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

5. 复用现有流程：

```text
calculate_metrics_from_points
draw_kendo_analysis_overlay
process_video
```

## 验证指标

每段测试视频记录：

- 总帧数
- 成功提取关键点帧数
- 关键点明显漂移帧数
- 左右手是否经常反
- 手腕点是否贴近真实手腕
- 肘点是否贴近真实肘部
- 输出视频主观评分：1 到 5 分

建议用同一段视频分别跑：

- MediaPipe baseline
- YOLO Pose nano
- YOLO Pose small 或 medium

## 成功标准

如果 YOLO Pose 在穿护具或拿竹刀时明显减少手腕、肘部漂移，就继续做 YOLO 后端。

如果 YOLO 仍然不稳定，但检测框和大关节点比 MediaPipe 好，可以进入第二阶段：标注剑道专用数据，训练自定义 YOLO Pose 模型。

## 风险

- 预训练 YOLO Pose 仍然是普通人体关键点，不理解护具和竹刀。
- 默认 17 点没有竹刀柄、剑尖、手部细节。
- 想真正适配剑道，最终可能需要自定义关键点标注和训练。

