# Unlimited Positional Arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 6, 7, 8))


def calculate(m, **kwargs):
    m += kwargs['add']
    m *= kwargs['multiply']
    print(m)


calculate(2, add=1, multiply=5)
