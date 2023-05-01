def rand_resize_crop(size:int, max_scale:float=2., ratios:Tuple[float,float]=(0.75,1.33)):
    "Randomly resize and crop the image to a ratio in `ratios` after a zoom of `max_scale`."
    return [zoom_squish(scale=(1.,max_scale,8), squish=(*ratios,8), invert=(0.5,8), row_pct=(0.,1.), col_pct=(0.,1.)),
            crop(size=size)]