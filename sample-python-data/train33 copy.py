def scatter_plot(data, x, y, by=None, ax=None, figsize=None, grid=False,
                 **kwargs):
    """
    Make a scatter plot from two DataFrame columns

    Parameters
    ----------
    data : DataFrame
    x : Column name for the x-axis values
    y : Column name for the y-axis values
    ax : Matplotlib axis object
    figsize : A tuple (width, height) in inches
    grid : Setting this to True will show the grid
    kwargs : other plotting keyword arguments
        To be passed to scatter function

    Returns
    -------
    matplotlib.Figure
    """
    import matplotlib.pyplot as plt

    kwargs.setdefault('edgecolors', 'none')

    def plot_group(group, ax):
        xvals = group[x].values
        yvals = group[y].values
        ax.scatter(xvals, yvals, **kwargs)
        ax.grid(grid)

    if by is not None:
        groups = data.groupby(by)
        fig, axes = plt.subplots(len(groups), 1, figsize=figsize, sharex=True, sharey=True)
        if len(groups) == 1:
            axes = [axes]
        for ax, (group_name, group) in zip(axes, groups):
            plot_group(group, ax)
            ax.set_ylabel(pprint_thing(y))
            ax.set_xlabel(pprint_thing(x))
            ax.set_title(pprint_thing(group_name))
            ax.grid(grid)
        fig.suptitle(by)

    else:
        fig, ax = plt.subplots(figsize=figsize)
        plot_group(data, ax)
        ax.set_ylabel(pprint_thing(y))
        ax.set_xlabel(pprint_thing(x))
        ax.grid(grid)

    return fig
