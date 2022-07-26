def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_word = ''
    for char in phrase:
        if char == phrase[0] and len(new_word) == 0:
            new_word += char.upper()
        else:
            new_word += char
    return new_word
