def print_formatted(number):
    if number <= 0:
        return []

    width = len(bin(number)) - 2
    result = []

    for i in range(1, number + 1):
        formatted = f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}"
        result.append(formatted)

    return result
