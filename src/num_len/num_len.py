def num_len(n):
    if n/10 < 1:
        return 1
    return 1 + num_len(n/10)