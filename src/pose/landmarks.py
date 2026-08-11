def get_landmark(result, landmark_index: int):
    if result.pose_landmarks is None:
        return None
    if result.pose_landmarks == []:
        return None
    
    landmark = result.pose_landmarks[0]
    if 0 <= landmark_index < len(landmark):
        return landmark[landmark_index]
    return None