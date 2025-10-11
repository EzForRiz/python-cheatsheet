age = int(input('please type your age:')) # wrap this with int() else it wont work.

if age >= 18:
    print("You're an adult!")
elif age <1:
    print("You're not even born yet!")

else:
    print("You're a minor!")


# This code first checks the user's age using if-elif-else statements and prints a message based on their input.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except:
    print("Oops! Something went wrong.")



# Then it demonstrates basic error handling with try-except — taking two numbers, dividing them, and catching any runtime errors (like dividing by zero or entering invalid input).
