# Step 1: Creating the Book class with attributes
class Book:
    def __init__(self, title, status="Available"):
        self.title = title
        self.status = status

    def display(self):
        print(self.title + " - " +  self.status)
        
    def borrow(self):
        if self.status == "Available":
            self.status = "Checked Out"
            print(self.title + " has been borrowed.")
        else:
            print(self.title + " is already checked out.")

# Creating book objects
book1 = Book("1984")
book2 = Book("The Hobbit", "Checked Out")
book3 = Book("Dune")  # Adding a new book


# Displaying the books
book1.display()
book2.display()
book3.display()


# Borrowing a book
book3.borrow()
book3.display()




#Example 2
class User:
    def __init__(self, username, display_name):
        self.username = username
        self.display_name = display_name
    
    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

class Post:
    def __init__(self, content, author):
        self.content = content  # Store the text of the post
        self.author = author  # Store the user who created it
        self.likes = [ ]  # List of users who liked the post
        
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(user.display_name + " liked this post!")

# Users
user1 = User("alex123", "Alex")
user2 = User("emma456", "Emma")

# Post
post1 = Post("Hello world!", user1)

# Liking the post
post1.like_post(user2)  # Emma likes Alex's post






#Redoing it 
class User:
    def __init__(self, username, display_name, bio=None):
        self.username = username
        self.display_name = display_name
        self.bio = bio  # optional bio attribute

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")
        if self.bio:
            print("Bio:", self.bio)
        print()  # spacing

    def create_post(self, content):
        post = Post(content, self)
        return post

    def like_post(self, post):
        post.like_post(self)
    
    def unlike_post(self, post):
        post.unlike_post(self)


class Post:
    def __init__(self, content, author):
        self.content = content  
        self.author = author  
        self.likes = [ ]
    
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")
    
    def unlike_post(self, user):
        if user in self.likes:
            self.likes.remove(user)
            print(user.display_name, "unliked this post!")
        else:
            print(user.display_name, "hasn't liked this post yet!")


# Testing
user1 = User("alex123", "Alex", "Love coding and coffee!")
user2 = User("cody8", "Cody", "Anime enthusiast ☕")

user1.show_profile()
user2.show_profile()

post1 = user1.create_post("This is my first Chirp!!!")
print(user1.display_name + " posted a chirp: " + post1.content)

user2.like_post(post1)
user2.unlike_post(post1)
user2.unlike_post(post1)




