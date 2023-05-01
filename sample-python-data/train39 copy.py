def _tilt(c, direction:uniform_int, magnitude:uniform=0, invert=False):
    "Tilt `c` field with random `direction` and `magnitude`."
    orig_pts = [[-1,-1], [-1,1], [1,-1], [1,1]]
    if direction == 0:   targ_pts = [[-1,-1], [-1,1], [1,-1-magnitude], [1,1+magnitude]]
    elif direction == 1: targ_pts = [[-1,-1-magnitude], [-1,1+magnitude], [1,-1], [1,1]]
    elif direction == 2: targ_pts = [[-1,-1], [-1-magnitude,1], [1,-1], [1+magnitude,1]]
    elif direction == 3: targ_pts = [[-1-magnitude,-1], [-1,1], [1+magnitude,-1], [1,1]]
    coeffs = _find_coeffs(targ_pts, _orig_pts) if invert else _find_coeffs(_orig_pts, targ_pts)
    return _apply_perspective(c, coeffs)