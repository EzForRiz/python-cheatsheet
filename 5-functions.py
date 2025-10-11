def greet():        # Define a new function
    print("Hello!") # What it does

greet()             # Call the function



def welcome(name):       #name is a parameter. we call them props in javascript.   
    print("welcome,", name)

welcome("Ava")
welcome("Zane")



def add(a, b):
    return a + b

result = add(5, 3)
print(result)


def madlib(noun, verb, adjective):
    input(noun)
    input(verb)
    input(adjective)
    print("The",adjective, noun, "decided to", verb, "all day.")

madlib("cat", "dance", "silly")



def noun():
    return 'Riz'

def verb():
    return 'Goat'


print('is', noun(), 'a', verb(), "?")
