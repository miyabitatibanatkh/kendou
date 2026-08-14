# Progress

## Current phase

Phase 7: 数据导出

## Completed

- 已有 README.md
- 创建基础目录结构
- 创建 requirements.txt
- 创建 .gitignore
- 已创建 Python 包初始化文件
- 创建虚拟环境 .venv
- 安装 requirements.txt 依赖
- 验证关键依赖 import 成功
- 创建 src/video/reader.py
- 实现 open_video 函数
- 验证不存在的视频路径会抛出 FileNotFoundError
- 验证真实视频可以成功打开
- 成功读取视频第一帧
- 成功获取视频 FPS、宽度、高度和总帧数
- 成功循环读取全部帧
- 实现 release_video 函数
- 验证视频资源可以正确释放
- 创建 src/video/writer.py
- 实现 create_video_writer 函数
- 验证 VideoWriter 可以成功创建
- 实现 write_frame 函数
- 验证可以写入一帧到输出视频
- 验证可以写入前 30 帧到输出视频
- 给 create_video_writer 添加打开失败检查
- 实现 release_writer 函数
- 验证 VideoWriter 可以正确释放
- 整理 Phase 2 代码格式
- 验证整理后仍可读取并写入一帧
- 创建 src/analysis/geometry.py
- 实现 midpoint 函数
- 验证 midpoint 可以计算两点中点
- 实现 distance 函数
- 验证 distance 可以计算两点距离
- 实现 angle_between_three_points 函数
- 验证 angle_between_three_points 可以计算三点夹角
- 实现 angle_from_vertical 函数
- 验证 angle_from_vertical 可以计算相对垂直线角度
- 已为 midpoint 编写单元测试
- 已为 distance 编写单元测试
- 已为 angle_between_three_points 编写单元测试
- 已为 angle_from_vertical 编写单元测试
- 已创建 src/pose/detector.py
- 已实现 create_pose_detector 函数
- 已下载 models/pose_landmarker.task 模型文件
- 验证 create_pose_detector 可以成功创建 PoseLandmarker
- 已创建 detect_pose 函数结构
- 已实现 detect_pose 函数
- 验证 detect_pose 可以处理一帧图像并返回 PoseLandmarkerResult
- 已实现 get_landmark 函数
- 已实现 get_landmark 函数
- 验证 get_landmark 在没有检测到人体时返回 None
- 已为 get_landmark 添加索引边界单元测试
- 验证 get_landmark 对负数和超出范围的索引返回 None
- 已实现 landmark_to_pixel 函数
- 已将归一化关键点坐标转换为像素坐标
- 已为 landmark_to_pixel 添加单元测试
- 验证 640×480 图像中的坐标 (0.25, 0.5) 可转换为 (160, 240)
- 已实现并测试关键点 visibility 可信度检查
- 已实现并测试 elbow angle 计算
- 已实现并测试 shoulder angle 计算
- 已实现并测试 body lean angle 计算
- 已实现并测试 hand center 计算
- 已实现并测试 hand center offset 计算
- 已实现并测试 hand height offset 计算
- 已实现并测试 frame-level kendo metrics 汇总
- 已实现并测试 draw_point 关键点绘制
- 已实现并测试 draw_line 骨架连线绘制
- 已实现并测试 draw_skeleton 基础骨架绘制
- 已定义并测试 KENDO_SKELETON_CONNECTIONS 默认骨架连接关系
- 已实现并测试 draw_kendo_skeleton 默认剑道骨架绘制
- 实现 draw_metrics_text 指标文本绘制
- 实现 draw_kendo_analysis_overlay 组合绘制骨架和指标文本
- 实现 extract_kendo_points，将 MediaPipe 关键点转换为像素坐标
- 实现 calculate_metrics_from_points，从关键点字典计算剑道指标
- 实现 process_detected_frame，处理单帧姿态结果并绘制分析信息
- 实现 process_video，逐帧检测姿态、绘制分析结果并写入输出视频
- 测试 process_video，可以逐帧处理并写入输出视频
- 创建 run_analysis.py，用真实 MediaPipe 模型处理输入视频
- 将 MediaPipe 检测改为视频模式，使用 timestamp_ms 逐帧检测
- 添加输出视频统计：总帧数、检测成功帧数、失败帧数、FPS、宽高
- 验证 heavy 模型对护具和背面视频提升有限
- 记录结论：通用视觉姿态模型对剑道护具、竹刀遮挡、背面视角不稳定
- 完成 Phase 6：结果可视化
- 实现 create_metric_row，将单帧分析指标转换为 CSV 行数据


## Current task

将每帧指标导出为 CSV
## Next task

在视频处理流程中收集每帧指标

## Problems

- MediaPipe 对穿护具、背面视角、竹刀遮挡和快速挥动不稳定
- heavy 模型提升有限，问题主要来自通用人体姿态模型不适配剑道场景

## Last verification

(.venv) E:\GitHub\kendou>python -m pytest
====================================================== test session starts =======================================================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: E:\GitHub\kendou
plugins: anyio-4.14.2
collected 31 items                                                                                                                

tests\test_csv_exporter.py ..                                                                                               [  6%]
tests\test_frame_processor.py ..                                                                                            [ 12%]
tests\test_geometry.py ....                                                                                                 [ 25%]
tests\test_kendo_metrics.py ..........                                                                                      [ 58%]
tests\test_landmarks.py .....                                                                                               [ 74%]
tests\test_overlay.py .......                                                                                               [ 96%]
tests\test_video_processor.py .                                                                                             [100%]

======================================================= 31 passed in 0.86s =======================================================