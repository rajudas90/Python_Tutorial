indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish: ")

if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("I don't know which cusine is this")

# if statement execute a block of code only if the condition is true, enabling conditional logic in programs.
# Use elif to specify additional conditions if the initial if condition fails, allowing for multiple sequential checks.
# else provides a fallback block of code when all preceding if and elif condition are false.
# Combine logical operators like and, or, and not within if statements to handle complex conditional expressions.
# Nested if statement allow for checking multiple layers of conditions, enabling detailed decision-making processes in code.
