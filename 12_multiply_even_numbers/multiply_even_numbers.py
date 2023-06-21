def multiply_even_numbers(nums):
    even_numbers = []
    result = 1
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)

    for num in even_numbers:
        result *= num

    return result

    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
