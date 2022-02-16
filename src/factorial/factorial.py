import logging

def factorial(n):
    if n < 0:
        logging.error("Error: factorial must be non-negative integer!")
        return logging.ERROR
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)