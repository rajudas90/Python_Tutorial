# Calculate total

expenses = [1200, 1300, 1500, 1700]

total_expense = 0
for expense in expenses:
    total_expense = total_expense + expense
print(total_expense)

# Print month wise value starting from month 1
total_expense = 0
for i in range(len(expenses)):
    expense = expenses[i]
    print(f"Month {i+1}, Expense is {expense}")
    total_expense += total_expense

print("Total Expense: ", total_expense)

# Shorter way to write same code using a built function "enumerate",
# this function will give both the element and index
total_expense = 0
for i, expense in enumerate(expenses):
    print(f"Month {i+1}, Expense is {expense}")
    total_expense += total_expense
print("Total Expense: ", total_expense)
