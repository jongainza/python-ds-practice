def reverse_vowels(s):
    vowels = set("aeiou")
    s_list = list(s)
    i = 0
    j = len(s) - 1
    while j > i:
        if s_list[i].lower() not in vowels:
            i += 1
        elif s_list[j].lower() not in vowels:
            j -= 1
        else:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

    return "".join(s_list)

    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
