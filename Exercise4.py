# Give the divisors of a certain number
number = int(input("Give me a number: "))
range = range(1, number+1)
result = []
for num in range:
    if number % num == 0:
        result.append(num)
print(result)