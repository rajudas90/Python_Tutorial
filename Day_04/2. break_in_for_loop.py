# Write a code where monthly sales first missed the target value

monthly_sales = [42, 38, 33, 38, 40, 45, 29]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

threshold = 35

for sales_amount, month in zip (monthly_sales, months):
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than the threshold in {month}")
        break
    else:
        print(f"Sales amount {sales_amount} is grater than the threshold in {month}")

# If we don't use break statement then the loop will go to the end.
# We use break statement to stop the loop where if statement satisfy.
# Ctrl + / is used to commenting & uncommenting code
# The zip() function in Python is a built-in function
# - that takes one or more iterables (such as lists, tuples, or strings)
# - as input and aggregates their corresponding elements into a single iterable of tuples.
