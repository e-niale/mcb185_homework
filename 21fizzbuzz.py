# loop to find divisible by 3, divisible by 5 and prints Fizz, Buzz, or both respectively 
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
