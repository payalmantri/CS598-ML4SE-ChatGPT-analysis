from heapq import heappop, heappush


def nlargest(n, iterable, key=None):
    """Find the n largest elements in a dataset.

    Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
    """
    if key is None:
        def key(x): return x

    heap = []
    for elem in iterable:
        if len(heap) < n:
            heappush(heap, (key(elem), elem))
        else:
            if key(elem) > heap[0][0]:
                heappop(heap)
                heappush(heap, (key(elem), elem))

    return [elem for _, elem in sorted(heap, reverse=True)]
