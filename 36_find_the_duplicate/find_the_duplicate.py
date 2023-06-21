def find_the_duplicate(nums):
    # if len(set(nums)) == len(nums):
    #     return None
    # coun = {}
    # for n in nums:
    #     coun[n] = coun.get(n, 0) + 1
    #     if coun[n] == 2:
    #         return n

    sen = set()
    for n in nums:
        if n in sen:
            return n
        sen.add(n)
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
