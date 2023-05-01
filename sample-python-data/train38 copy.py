def _symmetric_warp(c, magnitude:partial(uniform,size=4)=0, invert=False):
    "Apply symmetric warp of `magnitude` to `c`."
    m = listify(magnitude, 4)
    targ_pts = [[-1-m[3],-1-m[1]], [-1-m[2],1+m[1]], [1+m[3],-1-m[0]], [1+m[2],1+m[0]]]
    return _do_perspective_warp(c, targ_pts, invert)