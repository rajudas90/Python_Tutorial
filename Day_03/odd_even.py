n = int(input("Enter a number:"))

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
# int convert the input function as string to integer

# Compact way write the same code
message = "Number is even" if n % 2 == 0 else "Number is odd"
print (message)

#Using negate operator

if not n % 2 == 0:
    print(f"{n} is an odd number!")
else:
    print(f"{n} is an even number!")

# Use AND operator
if n > 10 and n % 2 == 0:
    print("Yes")
else:
    print("No")

# Use OR operator
a = int(input("Enter an another number:"))
if n > 10 or n % 2 == 0:
    print("Yes")
else:
    print("No")

