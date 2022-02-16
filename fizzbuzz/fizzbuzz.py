def fizzbuzz(n):
    for i in range(n):
        out = ""
        if i % 3 == 0: 
            out += "fizz"
        if i % 5 == 0:
            out += "buzz"
        else:
            out = i
        print(out)

fizzbuzz(100)