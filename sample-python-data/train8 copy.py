def face_locations(img, number_of_times_to_upsample=1, model="hog"):
    """
    Returns an array of bounding boxes of human faces in a image

    :param img: An image (as a numpy array)
    :param number_of_times_to_upsample: How many times to upsample the image looking for faces. Higher numbers find smaller faces.
    :param model: Which face detection model to use. "hog" is less accurate but faster on CPUs. "cnn" is a more accurate
                  deep-learning model which is GPU/CUDA accelerated (if available). The default is "hog".
    :return: A list of tuples of found face locations in css (top, right, bottom, left) order
    """
    if model not in ["hog", "cnn"]:
        raise ValueError(f"Invalid model '{model}'. Allowed models are 'hog' and 'cnn'.")

    raw_locations = _raw_face_locations(img, number_of_times_to_upsample, model)

    css_locations = []
    for face in raw_locations:
        if model == "cnn":
            css_locations.append(_trim_css_to_bounds(_rect_to_css(face.rect), img.shape))
        else:
            css_locations.append(_trim_css_to_bounds(_rect_to_css(face), img.shape))

    return css_locations
