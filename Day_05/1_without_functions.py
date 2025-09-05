# Total expenses of sergey & sundar

expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

# We can do using for loop (conventional way)

total_expense_sergey = 0
for expense in expenses_sergey:
    total_expense_sergey += expense
print("Total sergey's expense: ", total_expense_sergey)

total_expense_sundar = 0
for expense in expenses_sundar:
    total_expense_sundar  += expense
print("Total sundar's expense: ", total_expense_sundar)

# using this method is not efficient for long data. So we use functions that allows to reuse the code.


