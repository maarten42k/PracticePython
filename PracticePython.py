#Main script to run all other exercises
exercise = int(input("Which Exercise should I start? (1-30) "))
if exercise == 1:
    import Exercise1
elif exercise == 2:
    import Exercise2
elif exercise == 3:
    import Exercise3
elif exercise == 4:
    import Exercise4
elif exercise == 5:
    import Exercise5
elif exercise == 6:
    import Exercise6
else:
    print("This project does not exist!")