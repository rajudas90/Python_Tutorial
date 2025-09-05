def find_total(expenses):
    """
    :param expenses: input list containing numbers
    :return: total sum of all numbers from the input list
    """
    total = 0
    for expense in expenses:
        total += expense
    return total

expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

total_expense_sergey = find_total(expenses_sergey)
print("Total surgey's expenses is: ", total_expense_sergey)

total_expense_sundar = find_total(expenses_sundar)
print("Total sundal's expenses is: ", total_expense_sundar)

# to print the documentation
print(help(find_total))