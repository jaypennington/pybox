# Create a function that takes a number num and returns its length.
# The use of the len() function is prohibited


def num_len(n):
    if n/10 < 1:
        return 1
    return 1 + num_len(n/10)