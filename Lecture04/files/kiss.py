# Way more complex than needed...
def add_numbers(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a == 0 and b == 0:
        return 0
    elif a < 0 and b < 0:
        return a + b
    else:
        return a + b

# Simple version
def add_numbers(a, b):
    return a + b
