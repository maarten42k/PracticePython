# Impot the datetime module for the current year
import datetime

name_user = input("Hi, what is your name ? ")
age_user = input("Hi %s, how old are you ? " %name_user)
now = datetime.datetime.now()
year_100 = now.year + (100 - int(age_user))
output = "In %s you will be a whopping 100 years old!" %year_100
print(output + "\n")
number = int(input("Can you give me a number %s ? " %name_user))
# Print the message x number of times
for number_of_times in range(number):
    print(output)
