def adventure():
    print("You stand at a fork in the road.")
    choice = input("Do you go left or right? ")

    if choice == "left":
        print("You encounter a friendly dragon!")
    elif choice == "right":
        print("You find a hidden treasure chest!")
    else:
        print("You get lost in the woods.")

adventure()




def adventure2():
    print("You stand at a fork in the road.")
    choice = input("Do you go left or right? ")

    if choice == "left":
        print("You encounter a friendly dragon!")
        second = input("Do you talk to the dragon or walk away? ")
        if second == "talk":
            print("The dragon gives you a magical map!")
        elif second == "walk away":
            print("You safely head back home, a little disappointed.")
        else:
            print("The dragon flies off while you hesitate.")

    elif choice == "right":
        print("You find a hidden treasure chest!")
        second = input("Do you open it or leave it? ")
        if second == "open":
            print("You find gold and a mysterious key!")
        elif second == "leave":
            print("You walk away, wondering what might've been inside.")
        else:
            print("It disappears while you're thinking.")

    else:
        print("You get lost in the woods.")

adventure2()




# Modify the function below by adding more layers to make the story your own!
def jungle_adventure():
    # Ask the user to choose between two paths
    path = input("You find two paths: one goes to a river, the other to a mountain. Where do you go? ")

    # Check what the user typed and respond accordingly
    if path == "river":
        print("You swim with dolphins!")
    elif path == "mountain":
        print("You find an ancient temple!")
    else:
        # If the user typed something else, give this outcome
        print("You wander into the jungle and get lost.")

# Start the jungle adventure by calling the function
jungle_adventure()