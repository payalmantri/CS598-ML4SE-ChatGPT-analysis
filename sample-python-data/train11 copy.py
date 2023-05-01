def face_encodings(face_image, known_face_locations=None, num_jitters=1):
    """
    Given an image, return the 128-dimension face encoding for each face in the image.

    :param face_image: The image that contains one or more faces
    :param known_face_locations: Optional - the bounding boxes of each face if you already know them.
    :param num_jitters: How many times to re-sample the face when calculating encoding. Higher is more accurate, but slower (i.e. 100 is 100x slower)
    :return: A list of 128-dimensional face encodings (one for each face in the image)
    """
    face_encodings = []

    for face_location in known_face_locations:
        # Extract the face image from the original image
        top, right, bottom, left = face_location
        face_image_cropped = face_image[top:bottom, left:right]

        # Get the raw face landmarks of the cropped face image
        raw_landmarks = _raw_face_landmarks(face_image_cropped, model="small")

        # Calculate the face encoding for each face using the raw landmarks and specified number of jitters
        face_encoding = np.array(face_encoder.compute_face_descriptor(face_image_cropped, raw_landmarks[0], num_jitters))

        face_encodings.append(face_encoding)

    return face_encodings
