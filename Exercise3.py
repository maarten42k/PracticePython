# Small list of number
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
number = int(input("Give me a number: "))
# Make a new list where the numbers are smaller than the user input
for item in list:
    if item < number:
        new_list.append(item)
print(new_list)
