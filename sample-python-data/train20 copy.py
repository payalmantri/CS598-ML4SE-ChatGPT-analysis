def nsmallest(n, iterable, key=None):
    """Find the n smallest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key)[:n]
    """

    if n <= 0:
        return []

    if key is None:
        def key(x):
            return x

    heap = []
    for elem in iterable:
        heapq.heappush(heap, (key(elem), elem))
        if len(heap) > n:
            heapq.heappop(heap)

    return [elem for k, elem in sorted(heap)]
