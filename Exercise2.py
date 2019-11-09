# Get a number from the user
number = int(input("Give me a number: "))
if number % 4 == 0:
    print("This number is a multiple of 4!")
elif number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")
# Get a new number + the divider from the user
num = int(input("Now give me another number: "))
check = int(input("And give me a divider: "))
if num % check == 0:
    print("%d can be divided by %d." % (num , check))
else:
    print("It is not possible to divide %d by %d." % (num, check))
