# ChatGPT generated
def load_image_file(file, mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array

    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    """
    try:
        with open(file, 'rb') as f:
            image_bytes = f.read()
    except:
        raise ValueError(f"Unable to open file '{file}'")

    try:
        pil_image = Image.open(BytesIO(image_bytes)).convert(mode)
    except:
        raise ValueError(f"Unable to open image in file '{file}'")
    
    return np.array(pil_image)
