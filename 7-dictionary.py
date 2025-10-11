person = {
    "name": "Ava",
    "age": 25,
    "city": "Seattle"
}

person["job"] = "Engineer"  # Added new key-value pair
person["age"] = 26          # Updated existing value


print(person)

# print(person["name"])


for key, value in person.items():
    print(key.title(), ":", value)



contacts = {
    "Mom": "555-1234",
    "Best Friend": "555-5678",
    "Pizza Place": "555-9999"
}

print("Call Pizza Place at", contacts["Pizza Place"])



# Dictionaries store data as key-value pairs. You can add new keys, update existing ones, access values using keys, and loop through all items with .items().


# In the contacts example, you can directly access a value (like a phone number) using its key inside square brackets.
