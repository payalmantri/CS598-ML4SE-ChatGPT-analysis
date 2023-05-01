import cv2

def _raw_face_locations(img, number_of_times_to_upsample=1, model="hog"):
    """
    Returns an array of bounding boxes of human faces in a image

    :param img: An image (as a numpy array)
    :param number_of_times_to_upsample: How many times to upsample the image looking for faces. Higher numbers find smaller faces.
    :param model: Which face detection model to use. "hog" is less accurate but faster on CPUs. "cnn" is a more accurate
                  deep-learning model which is GPU/CUDA accelerated (if available). The default is "hog".
    :return: A list of dlib 'rect' objects of found face locations
    """
    if len(img.shape) == 2:  # check if image is grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # convert grayscale to RGB

    if model == "cnn":
        face_locations = cnn_face_detector(img, number_of_times_to_upsample)
    else:
        face_locations = face_detector(img, number_of_times_to_upsample)

    return [(top(), right(), bottom(), left()) for top, right, bottom, left in face_locations]
