def batch_face_locations(images, number_of_times_to_upsample=1, batch_size=128):
    """
    Returns an 2d array of bounding boxes of human faces in a image using the cnn face detector
    If you are using a GPU, this can give you much faster results since the GPU
    can process batches of images at once. If you aren't using a GPU, you don't need this function.

    :param img: A list of images (each as a numpy array)
    :param number_of_times_to_upsample: How many times to upsample the image looking for faces. Higher numbers find smaller faces.
    :param batch_size: How many images to include in each GPU processing batch.
    :return: A list of tuples of found face locations in css (top, right, bottom, left) order
    """

    def get_css_faces_batch(batch):
        detections = _raw_face_locations_batched(batch, number_of_times_to_upsample, 1)
        return [_trim_css_to_bounds(_rect_to_css(face.rect), batch[0].shape) for face in detections[0]]

    batches = [images[i:i+batch_size] for i in range(0, len(images), batch_size)]
    css_faces = []

    for batch in batches:
        css_faces_batch = get_css_faces_batch(batch)
        css_faces.extend(css_faces_batch)

    return css_faces
