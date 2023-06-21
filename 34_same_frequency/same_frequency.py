def same_frequency(num1, num2):
    str1 = str(num1)
    str2 = str(num2)

    def freq_counter(string):
        count = {}
        for s in string:
            count[s] = count.get(s, 0) + 1
        return count

    return freq_counter(str1) == freq_counter(str2)

    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
