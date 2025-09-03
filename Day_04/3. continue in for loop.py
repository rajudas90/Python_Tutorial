# continue is like opposite of the break statement
# The continue statement in Python is a loop control statement
# used to skip the rest of the current iteration of a loop
# and proceed to the next iteration.
# When the continue statement is encountered within a loop (either for or while),
# the code within the loop that follows the continue statement is skipped for that specific iteration,
# and the loop immediately moves to evaluate the condition for the next iteration.

# Print odd numbers
for i in range(1,11):
    if i % 2 != 0:
        print(i)

# Print odd numbers using continue
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)