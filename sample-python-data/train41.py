def _compute_zs_mat(sz:TensorImageSize, scale:float, squish:float,
                   invert:bool, row_pct:float, col_pct:float)->AffineMatrix:
    "Utility routine to compute zoom/squish matrix."
    orig_ratio = math.sqrt(sz[1]/sz[0])
    for s,r,i in zip(scale,squish, invert):
        s,r = 1/math.sqrt(s),math.sqrt(r)
        if s * r <= 1 and s / r <= 1: #Test if we are completely inside the picture
            w,h = (s/r, s*r) if i else (s*r,s/r)
            col_c = (1-w) * (2*col_pct - 1)
            row_c = (1-h) * (2*row_pct - 1)
            return _get_zoom_mat(w, h, col_c, row_c)

    #Fallback, hack to emulate a center crop without cropping anything yet.
    if orig_ratio > 1: return _get_zoom_mat(1/orig_ratio**2, 1, 0, 0.)
    else:              return _get_zoom_mat(1, orig_ratio**2, 0, 0.)