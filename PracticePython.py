#Main script to run all other exercises
exercise = int(input("Which Exercise should I start? (1-30) "))
if exercise == 1:
    import Exercise1
elif exercise == 2:
    import Exercise2
else:
    print("This project does not exist!")