def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    max = 0
    # for num in nums:
    #     if nums.count(num) > max:
    #         max = num
    # return max

    #0(n^2) try o(n)

    freq_count = {}
    for num in nums:
        freq_count[num] = nums.count(num)

    for num in freq_count:
        if freq_count[num] > max:
            max = num

    return max

