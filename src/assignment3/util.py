def find_runner_up(arr):
    unique_scores = list(set(arr))
    
    if len(unique_scores) < 2:
        return None

    unique_scores.sort()
    return unique_scores[-2]
