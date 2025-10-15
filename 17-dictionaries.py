fitness_list1 = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
fitness_list2 = ["Ulises", 347, 625, 729, 977, 0, 0, 0]
fitness_list3 = ["Christine", 214, 665, 373, 1095, 349, 1037, 0]

key1 = fitness_list1[0]
value1 = fitness_list1[1:]
key2 = fitness_list2[0]
value2 = fitness_list2[1:]
key3 = fitness_list3[0]
value3 = fitness_list3[1:]

fitness_dictionary = {}
fitness_dictionary[key1] = value1
fitness_dictionary[key2] = value2
fitness_dictionary[key3] = value3

for user in fitness_dictionary:
    print(user, "took following steps per day: ", fitness_dictionary[user])




#refer to code below to understand the basics of dictionaries

# fitness_list = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
# print("List looks like ", fitness_list)

# key = fitness_list[0]
# value = fitness_list[1:]

# fitness_dictionary = {}
# fitness_dictionary[key] = value

# print("Dictionary looks like", fitness_dictionary)






# Reading data from a file
data = numpy.loadtxt("steps.csv", delimiter = ",", dtype = str)

# Adding data to dictionary
data_dict = {}
for i in range(1, len(data)): # Choosing 1 instead of 0 to skip the header row
    row = data[i] # <--- Picking out a list from data
    name = row[0] # <--- Extracting name
    steps = numpy.array(row[1:], dtype = int) # <--- Extracting list of steps as integer
    data_dict[name] = steps # <--- Adding key:value pair to the dictionary

print(data_dict)
print(len(data_dict))  # Should print 10 if there are 10 users
print(len(data_dict["Jasmin"]))  # Should print 168 if Jasmin has 168 step values



