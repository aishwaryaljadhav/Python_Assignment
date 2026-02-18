def mutate_string(string, position, character):
    if position < 0 or position >= len(string):
        return None

    lst = list(string)
    lst[position] = character
    return "".join(lst)
