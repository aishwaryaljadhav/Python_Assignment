import math

def probability_at_least_one_a(n, letters, k):
    count_a = letters.count('a')
    non_a = n - count_a

    if k > non_a:
        return 1.0

    prob_no_a = math.comb(non_a, k) / math.comb(n, k)

    return 1 - prob_no_a
