import mediapipe as mp

def create_pose_detector():
    pose = mp.solutions.pose.Pose(
        static_image_mode=False,    
    )
    return pose 