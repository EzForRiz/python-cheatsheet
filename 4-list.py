fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I love", fruit)

favorites = ["reading", "coding", "travel"]

for item in favorites:
    print("One of my favorite things is", item)


#lists are similar to arrays in python but more flexible

# This code uses 'for' loops to go through each element in a list — one by one — and store it in a loop variable (like 'fruit' or 'item').


# Inside the loop, the 'print()' statement runs for every list item, letting you display or use each value individually.




week_without_Saturday = ["Sunday" , "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(week_without_Saturday)

week_without_Saturday.append("Saturday")
print(week_without_Saturday)

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
print(fitness_data)

first_index = 0
print(fitness_data[first_index])

last_index = len(fitness_data) - 1     #  arrays have index from 0 - i. so its 0-7 in this case. total are 8 values so 8-1 = 7  
print(fitness_data[last_index])

fitness_data.remove("Juliana")
print(fitness_data)


# this is for data science as lists are better than variables for storing alot of data


