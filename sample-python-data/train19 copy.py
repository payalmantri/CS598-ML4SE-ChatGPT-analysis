from heapq import merge as merge_sorted

def merge(iterables, key=None, reverse=False):
    '''Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

    If *key* is not None, applies a key function to each element to determine
    its sort order.

    >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
    ['dog', 'cat', 'fish', 'horse', 'kangaroo']

    '''

    def get_next(iterable):
        try:
            value = next(iterable)
        except StopIteration:
            value = None
        return value

    iterables = [iter(iterable) for iterable in iterables]
    if key is not None:
        iterables = [[(key(value), value) for value in iterable] for iterable in iterables]
    if reverse:
        iterables = [reversed(iterable) for iterable in iterables]
    merged = merge_sorted(*iterables)
    for _, value in merged:
        yield value
