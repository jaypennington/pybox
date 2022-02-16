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