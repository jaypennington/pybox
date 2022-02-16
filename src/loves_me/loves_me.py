# "Loves me, loves me not" is a traditional game in which a
# person plucks off all the petals of a flower one by one,
# saying the phrase "Loves me" and "Loves me not" when
# determining whether the one that they love, loves them back.

# Given a number of petals, return a string which repeats the
# phrases "Loves me" and "Loves me not" for every alternating
# petal, and return the last phrase in all caps. Remember to
# put a comma and space between phrases.


def loves_me(n):
    out = ""
    if n == 0:
        return "NO ONE LOVES YOU!"
    for i in range(n):
        if i % 2 == 0:
            if i == n-1:
                out += "LOVES ME!"
            else:
                out += "Loves me, "
        elif i % 1 == 0:
            if i == n-1:
                out += "LOVES ME NOT!"
            else:
                out += "Loves me not, "
    return out