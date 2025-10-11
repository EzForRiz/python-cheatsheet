# ---- First Example ----

name = input("Name: ")                  # Ask the user to type their name and store it in 'name'
fav_food = "Pizza"                      # Store favorite food in a variable
pet = 'dre'                             # Store pet’s name in a variable

print("Hi", name, "! Enjoy your", fav_food, "with your pet", pet, "!")     # Print a friendly message using variables and text



# ---- Second Example ----

name = input("Name: ")                  # Ask for the user's name again
Question = input('what are u doing? ')  # Ask what the user is doing right now
Music = 'Walk em Down'                  # Store a music name in a variable
drink = "pepsi"                         # Store a drink name in a variable

print("Hi", name, "! Enjoy your", Music, "with your", drink, "while", Question)      # Print a sentence combining user input and stored values



# ---- Third Section (Age Calculation) ----

birth_year = input("What year were you born? ")  # Ask for the user's birth year (input returns a string)
current_year = 2025                              # Store the current year as a number
age = current_year - int(birth_year)             # Convert 'birth_year' from string to int and calculate the age

print("You are about", age, "years old!")        # Print the calculated age as a complete sentence
