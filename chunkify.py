from itertools import zip_longest
from typing import List


# Write a function to group characters from an input string into fixed
# length chunks, with a given fill value, e.g.
# chunkify(‘ABCDEFG’, 3, ‘x’) -> [‘ABC’, ‘DEF’, Gxx’]
# Adapted from the grouper recipe found in the itertools documentation:
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def chunkify(s: str, chunk_size: int, fill: str = 'x') -> List[str]:

    if len(fill) != 1:
        raise ValueError('The fill string must consist of exactly one character')

    if chunk_size < 1:
        raise ValueError('The chunk size must be positive')

    if len(s) < chunk_size:
        return [s.ljust(chunk_size, fill)]

    args = [iter(s)] * chunk_size
    return [''.join(chars) for chars in list(zip_longest(*args, fillvalue=fill))]
