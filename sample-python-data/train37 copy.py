def _perspective_warp(c, magnitude:partial(uniform,size=8)=0, invert=False):
    "Apply warp of `magnitude` to `c`."
    magnitude = magnitude.view(4,2)
    targ_pts = [[x+m for x,m in zip(xs, ms)] for xs, ms in zip(_orig_pts, magnitude)]
    return _do_perspective_warp(c, targ_pts, invert)