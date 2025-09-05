# A lambda function is a small, one-line function without a name.

# square of number using functions without lambda
def find_square(a):
    return a*a
x = find_square(5)
print("Square without lambda", x)

# square of number using lambda
y = lambda b:b*b
print("Square using lambda", y(6))

# add two numbers using lambda
z = lambda c,d:c+d
print("Addition is:",z(5,7))
