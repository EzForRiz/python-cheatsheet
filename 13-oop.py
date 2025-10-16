# Step 1: Creating the Book class with attributes. A class is like a blueprint for creating objects.
class Book:
    def __init__(self, title, status="Available"):   #function
        self.title = title
        self.status = status

    def display(self):                               #function
        print(self.title + " - " +  self.status)
        
    def borrow(self):                                #function
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







# Chirpy posts platform 

# user class
import random
from post import Post  # We'll define Post later

class User:
    total_users = 0      # Class attribute: tracks total users
    max_posts = 5        # Class attribute: max posts per user

    def __init__(self, username, display_name):
        self.username = username          # Instance attribute
        self.display_name = display_name
        self.posts = []                  # List to store user's posts
        User.total_users += 1

    # Instance method: display profile
    def show_profile(self):
        print(f"User: {self.display_name} (@{self.username})")

    # Instance method: create post
    def create_post(self, content):
        if len(self.posts) >= User.max_posts:
            print(f"{self.display_name} has reached the post limit!")
            return None
        post = Post(content, self)
        self.posts.append(post)
        return post

    # Instance method: like a post
    def like_post(self, post):
        post.like_post(self)

    # Instance method: unlike a post
    def unlike_post(self, post):
        post.unlike_post(self)

    # Class method: create a guest user
    @classmethod
    def create_guest_user(cls):
        username = "guest" + str(random.randint(100, 999))
        return cls(username, "Guest")


#post class 

class Post:
    total_posts = 0       # Class attribute: tracks total posts
    MAX_CONTENT_LENGTH = 280  # Max characters per post

    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []      # List of users who liked this post
        Post.total_posts += 1

    # Instance method: like a post
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(f"{user.display_name} liked this post!")
        else:
            print(f"{user.display_name} has already liked this post!")

    # Instance method: unlike a post
    def unlike_post(self, user):
        if user in self.likes:
            self.likes.remove(user)
            print(f"{user.display_name} unliked this post.")
        else:
            print(f"{user.display_name} hasn't liked this post yet!")

    # Static method: validate content length
    @staticmethod
    def validate_content_length(content):
        return len(content) <= Post.MAX_CONTENT_LENGTH



# putting it all together

# Create regular users
user1 = User("alex123", "Alex")
user2 = User("emma456", "Emma")

# Create a guest user using class method
guest = User.create_guest_user()

# Show profiles
user1.show_profile()
user2.show_profile()
guest.show_profile()

# Users creating posts
post1 = user1.create_post("Hello world! My first chirp!")
post2 = user2.create_post("Excited to join Chirpy!")
post3 = guest.create_post("I am a guest user posting!")

# Users liking posts
user1.like_post(post2)
guest.like_post(post1)
user2.like_post(post3)

# Users unliking posts
guest.unlike_post(post1)   # Remove like
guest.unlike_post(post1)   # Try removing again

# Test static method
print("Is post1 length valid?", Post.validate_content_length(post1.content))

# Show totals
print("Total users:", User.total_users)
print("Total posts:", Post.total_posts)

# Test max post limit
for i in range(6):
    user1.create_post(f"Post #{i+2}")  # Should block after 5 posts
