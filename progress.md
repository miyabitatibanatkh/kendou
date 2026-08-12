# Progress

## Current phase

Phase 4：人体姿态识别

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

## Current task

实现剑道基础指标计算

## Next task

计算肩/肘/身体前倾角度

## Problems

## Last verification

(.venv) E:\GitHub\kendou>python -m pytest
===================================== test session starts ======================================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: E:\GitHub\kendou
plugins: anyio-4.14.2
collected 7 items                                                                               

tests\test_geometry.py ....                                                               [ 57%]
tests\test_landmarks.py ...                                                               [100%]

====================================== 7 passed in 0.05s =======================================