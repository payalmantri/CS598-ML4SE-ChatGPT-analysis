def hist_frame(data, column=None, by=None, grid=True, xlabelsize=None,
               xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False,
               sharey=False, figsize=None, layout=None, bins=10, **kwds):

    if by is not None:
        axes = grouped_hist(data, column=column, by=by, ax=ax, grid=grid,
                            figsize=figsize, sharex=sharex, sharey=sharey,
                            layout=layout, bins=bins, xlabelsize=xlabelsize,
                            xrot=xrot, ylabelsize=ylabelsize,
                            yrot=yrot, **kwds)
        return axes

    if column is not None:
        if not isinstance(column, (list, np.ndarray, ABCIndexClass)):
            column = [column]
        data = data[column]
    data = data._get_numeric_data()

    fig, axes = _subplots(naxes=len(data.columns), ax=ax, squeeze=False,
                          sharex=sharex, sharey=sharey, figsize=figsize,
                          layout=layout)

    for ax, col in zip(axes.flatten(), com.try_sort(data.columns)):
        ax.hist(data[col].dropna().values, bins=bins, **kwds)
        ax.set_title(col)
        ax.grid(grid)

    _set_ticks_props(axes, xlabelsize=xlabelsize, xrot=xrot,
                     ylabelsize=ylabelsize, yrot=yrot)

    fig.subplots_adjust(wspace=0.3, hspace=0.3)

    return axes
