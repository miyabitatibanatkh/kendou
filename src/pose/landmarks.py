KENDO_LANDMARK_INDICES = {
    "left_shoulder": 11,
    "right_shoulder": 12,
    "left_elbow": 13,
    "right_elbow": 14,
    "left_wrist": 15,
    "right_wrist": 16,
    "left_hip": 23,
    "right_hip": 24,
}


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


def is_landmark_visible(landmark, min_visibility : float = 0.5) -> bool:
    if landmark is None:
        return False

    visibility = getattr(landmark, 'visibility', None)
    if visibility is None:
        return False

    return visibility >= min_visibility


def extract_kendo_points(result, frame_width: int, frame_height: int, min_visibility: float = 0.5):
    points = {}

    for name, index in KENDO_LANDMARK_INDICES.items():
        landmark = get_landmark(result, index)

        if not is_landmark_visible(landmark, min_visibility):
            return None

        points[name] = landmark_to_pixel(landmark, frame_width, frame_height)

    return points


