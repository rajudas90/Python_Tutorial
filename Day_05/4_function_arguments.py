# *args → Variable Positional Arguments
# *args lets you pass any number of positional arguments to a function.
# Inside the function, args behaves like a tuple.
# Use *args when you don’t know how many arguments will be passed.

def sum_all(*args):
    print("Arguments received: ", args)
    total = 0
    for num in args:
        total += num
    return total

total_1 = sum_all(1,5,7,4,6,)
print("Sum of all arguments: ", total_1)

total_2 = sum_all(10,50,70,40,60,)
print("Sum of all arguments: ", total_2)