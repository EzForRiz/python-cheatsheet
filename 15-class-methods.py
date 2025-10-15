#   2 Methods in oop:

# Class Method

# Static Method

# First Parameter of Class Method:

# cls (class reference)

# First Parameter of Static Method:

# None

# Access of Class Method:

# Can modify class-level data

# Access of static Method:

# No access to class/instance data

# Use Case of class and static methods:

# Factory methods, class-wide logic (classmethod)

# Pure utility/validation functions (static methods)


# class methods
class User:
    total_users = 0  # Class attribute to track number of users

    @classmethod
    def create_guest_user(cls):
        # Generates a guest user with a random username
        guest = cls(username="guest_123", display_name="Guest")
        return guest


#   static methods
class Post:  
    MAX_CONTENT_LENGTH = 280  

    @staticmethod  
    def validate_content_length(content):  
        # Checks if a post meets the platform's character limit  
        return len(content) <= Post.MAX_CONTENT_LENGTH  






# Post.py:
class Post:
    total_posts = 0  # Class attribute

    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = [ ]
        Post.total_posts += 1

    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    # Static method to validate the length of a chirp
    @staticmethod
    def validate_content_length(content):
        if len(content) <= 280:
            return True
        else:
            return False




# main.py:
from user import User
from post import Post

# Creates a guest user
guest = User.create_guest_user()

# Test static method for chirp validation
test_chirp = guest.create_post("This is a sample chirp!")
print("Is chirp's length valid:", Post.validate_content_length(test_chirp.content))  # Expected: True






# user.py:
from post import Post  # Import the Post class
import random

class User:
    total_users = 0  # Class attribute

    def __init__(self, username, display_name):
        self.username = username
        self.display_name = display_name
        self.posts = [ ]
        User.total_users += 1

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.like_post(self)

    # Class method to create a guest user with a random username
    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        username = "guest" + str(random_number)
        display_name = "Guest"  # Default display name
        return cls(username, display_name)