people = [
    {"name": "Ava", "age": 25},
    {"name": "Zane", "age": 30},
    {"name": "Maya", "age": 22}
]

for person in people:
    print(person["name"], "is", person["age"], "years old.")




books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

for book in books:
    print(book['title'] , " by " , book['author'])




students = [
    {"name": "Ava", "age": 20, "score": '90'},
    {"name": "Zane", "age": 21, "score": '90'}
]

for candidate in students:
    print(candidate['name'], 'with', candidate['score'])





# Each dictionary in a list represents a single record (like a person, book, or student), and you can access its values using keys inside a loop.


# The 'for' loop goes through every dictionary in the list, letting you print or manipulate each record’s information individually.
