def _trim_css_to_bounds(css, image_shape):
    """
    Make sure a tuple in (top, right, bottom, left) order is within the bounds of the image.

    :param css:  plain tuple representation of the rect in (top, right, bottom, left) order
    :param image_shape: numpy shape of the image array
    :return: a trimmed plain tuple representation of the rect in (top, right, bottom, left) order
    """
    top, right, bottom, left = css
    max_top = min(top, image_shape[0])
    max_right = min(right, image_shape[1])
    max_bottom = max(bottom, 0)
    max_left = max(left, 0)
    return max_top, max_right, max_bottom, max_left
