def compact(lst):
    new_lst = []
    for v in lst:
        if v:
            new_lst.append(v)
    return new_lst
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
