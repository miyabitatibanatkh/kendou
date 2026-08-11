def get_landmark(result, landmark_index: int):
    if result.pose_landmarks is None:
        return None
    if result.pose_landmarks == []:
        return None
    
    landmark = result.pose_landmarks[0]
    if 0 <= landmark_index < len(landmark):
        return landmark[landmark_index]
    return None


def landmark_to_pixel(landmark, frame_width: int, frame_height: int):
    pixel_x = int(landmark.x * frame_width)
    pixel_y = int(landmark.y * frame_height)
    return pixel_x, pixel_y