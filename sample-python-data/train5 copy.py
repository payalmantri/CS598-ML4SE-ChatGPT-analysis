def face_distance(face_encodings, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.

    :param faces: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A list with the distance for each face in the same order as the 'faces' array
    """
    distances = []
    for encoding in face_encodings:
        distance = np.linalg.norm(encoding - face_to_compare)
        distances.append(distance)
    
    return distances
