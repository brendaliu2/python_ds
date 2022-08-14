def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_word = ''

    for char in phrase:
        if char == to_swap.lower():
            new_word += char.upper()
        elif char == to_swap.upper():
            new_word += char.lower()
        else:
            new_word += char
    return new_word

#swap case method