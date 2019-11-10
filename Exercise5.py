# Return the common values between these two lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

a = random.sample(range(20), 10)
b = random.sample(range(20), 10)
a.sort()
b.sort()
output = []
print("List A: " + str(a))
print("List B: " + str(b))
for number in a:
    if number in b and number not in output:
        output.append(number)
print("\nCommon values: " + str(output))
