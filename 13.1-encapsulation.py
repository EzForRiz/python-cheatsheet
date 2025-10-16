# Encapsulation means bundling data and the methods that act on that data into one object, while hiding internal details so they aren’t directly accessible from the outside.


# read this for some understanding before reading below code:

# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # Public attribute
        self._balance = balance    # Private attribute (convention: start with _)

    # Getter for balance
    @property
    def balance(self):
        return self._balance

    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount

# Usage
account = BankAccount("Alice", 1000)
print(account.balance)  # Access through getter
account.balance = 500   # Update through setter
account.balance = -100  # Validation prevents this






# below is a project code.


# =====================================================
# user.py
# =====================================================
# This section defines the User class.
# Encapsulation: Sensitive info like password is private.
# Properties: display_name has getter/setter with validation.
# Class method: create_guest_user uses `random` to make a random guest username.

import random  # Needed only for generating guest usernames

class User:
    total_users = 0  # Tracks total number of users

    def __init__(self, username, display_name, password):
        self.username = username
        self._display_name = display_name  # Private attribute
        self._password = password          # Private attribute
        self.posts = []                    # List of posts created by this user
        User.total_users += 1

    # Getter for display_name
    @property
    def display_name(self):
        return self._display_name

    # Setter for display_name with validation
    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")
        self._display_name = value

    # Print profile info
    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    # Create a new post
    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    # Like a post
    def like_post(self, post):
        post.like_post(self)

    # Class method to create guest users
    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        username = "guest" + str(random_number)
        display_name = "Guest"
        return cls(username, display_name, "guestpass")

    # Change password with validation
    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    # Check password
    def check_password(self, input_password):
        return input_password == self._password


# =====================================================
# comment.py
# =====================================================
# This section defines the Comment class.
# Each comment has a text and a commenter (User who commented).

class Comment:
    def __init__(self, text, commenter):
        self.text = text               # The text content of the comment
        self.commenter = commenter     # The User who made the comment

    # Display comment nicely
    def display_comment(self):
        print(self.commenter.display_name + " commented: '" + self.text + "'")


# =====================================================
# post.py
# =====================================================
# This section defines the Post class.
# Encapsulation: _content and _like_count are private.
# Properties and static methods are used for validation and safe access.

class Post:
    total_posts = 0  # Tracks total number of posts

    def __init__(self, content, author):
        self._content = content       # Private attribute for encapsulation
        self.author = author
        self.likes = []               # Public list of Users who liked the post
        self._like_count = 0          # Private like count
        self.comments = []            # List of Comment objects
        Post.total_posts += 1

    # Getter for post content
    @property
    def content(self):
        return self._content

    # Setter for post content with validation
    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")
        self._content = new_content

    # Like the post
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    # Getter for private like count
    def get_like_count(self):
        return self._like_count

    # Add a comment to the post
    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)
        self.comments.append(comment)
        print(comment.commenter.display_name, "added a comment on", self.author.display_name + "'s post.")
        return comment

    # Static method to validate content length without creating a post
    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280


# =====================================================
# socialnetwork.py
# =====================================================
# This section defines SocialNetwork class.
# It stores Users and Posts and provides methods for searching, removing, and listing.

class SocialNetwork:
    def __init__(self):
        self.users = []  # List of User objects
        self.posts = []  # List of Post objects

    # Add a user if username not already taken
    def add_user(self, user):
        if self.search_user_by_username(user.username):
            print("\nUser with username", user.username, "already exists!\n")
        else:
            self.users.append(user)
            print(user.display_name, "has been added to Chirpy.")

    # Add a post to the network
    def add_post(self, post):
        self.posts.append(post)
        print("A new post has been added to the Chirpy.")

    # Search user by username
    def search_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    # Remove user by username
    def remove_user(self, username):
        user_to_remove = self.search_user_by_username(username)
        if user_to_remove:
            self.users.remove(user_to_remove)
            print("\n", user_to_remove.display_name, "has been removed from the Chirpy.")
        else:
            print("\nUser with username", username, "not found!")

    # List all posts in the network
    def list_all_posts(self):
        if not self.posts:
            print("\nNo posts to display.")
        else:
            for post in self.posts:
                print(post.author.display_name + " posted: '" + post.content + "'")


# =====================================================
# main.py
# =====================================================
# This section tests all classes and demonstrates encapsulation, properties, likes, and comments.

# Create users
user1 = User("alex123", "Alex", "secret123")
user2 = User("emma456", "Emma", "password456")
guest = User.create_guest_user()

# Show profiles
user1.show_profile()
user2.show_profile()
guest.show_profile()

# Test display_name validation
try:
    user1.display_name = ""
except ValueError as e:
    print("Error:", e)

try:
    user1.display_name = "A very long display name that exceeds limits"
except ValueError as e:
    print("Error:", e)

user1.display_name = "AlexTheGreat"
user1.show_profile()

# Create posts and test content validation
post1 = user1.create_post("Hello world! This is my first chirp.")
print("Post content:", post1.content)

try:
    post1.content = "x" * 300
except ValueError as e:
    print("Error:", e)

# Like a post
user1.like_post(post1)
guest.like_post(post1)
print("Likes on post1:", post1.get_like_count())

# Test SocialNetwork
chirpy_network = SocialNetwork()
chirpy_network.add_user(user1)
chirpy_network.add_user(user2)
chirpy_network.add_user(guest)
chirpy_network.add_post(post1)
chirpy_network.list_all_posts()













# below is some code for understanding how this was built.

# user Class with Encapsulation
class User:
    total_users = 0

    def __init__(self, username, display_name, password):
        self.username = username
        self.display_name = display_name
        self._password = password  # private
        self.posts = [ ]
        User.total_users += 1

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password

# example usage
user1 = User("alex123", "Alex", "secret123")
print(user1._password)          # Works but discouraged
print(user1.check_password("secret123"))  # True
user1.change_password("newSecret")
print(user1.check_password("newSecret"))  # True





# Post Class with Encapsulation
class Post:
    total_posts = 0

    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = [ ]         # Public list of users
        self._like_count = 0     # Private attribute
        Post.total_posts += 1

    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    def get_like_count(self):
        return self._like_count   # Safe access to private data

    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280

# Example usage:

post1 = user1.create_post("Hello world!")
post1.like_post(user1)
print(post1.get_like_count())  # 1
post1.like_post(user1)          # Already liked



# main.py

from user import User
from post import Post

# 1️⃣ Create regular users
user1 = User("alex123", "Alex", "secret123")
user2 = User("emma456", "Emma", "mypassword")

# 2️⃣ Show profiles
user1.show_profile()
user2.show_profile()

# 3️⃣ Create a guest user using class method
guest = User.create_guest_user()
guest.show_profile()

# 4️⃣ Users create posts
post1 = user1.create_post("Hello world! This is my first chirp!")
post2 = guest.create_post("I am a guest user posting my first chirp!")

# 5️⃣ Users like posts
user1.like_post(post2)  # Alex likes guest's post
guest.like_post(post1)  # Guest likes Alex's post
user2.like_post(post1)  # Emma likes Alex's post

# 6️⃣ Access like counts safely (encapsulation)
print(post1.author.display_name + "'s post has", post1.get_like_count(), "likes")
print(post2.author.display_name + "'s post has", post2.get_like_count(), "likes")

# 7️⃣ Test password access and updates (encapsulation)
print("Checking Alex's password:", user1.check_password("secret123"))  # True
user1.change_password("newSecret123")
print("Checking Alex's new password:", user1.check_password("newSecret123"))  # True

# 8️⃣ Validate chirp content length (static method)
long_chirp = "x" * 300
print("Is long chirp valid?", Post.validate_content_length(long_chirp))  # False
short_chirp = "Hello, this is short!"
print("Is short chirp valid?", Post.validate_content_length(short_chirp))  # True

# 9️⃣ Display total users and total posts (class attributes)
print("Total users on Chirpy:", User.total_users)
print("Total posts on Chirpy:", Post.total_posts)





# user.py
from post import Post
import random

class User:
    total_users = 0  # Class attribute to track total users

    def __init__(self, username, display_name, password):
        self.username = username
        self.display_name = display_name
        self._password = password  # Private attribute for encapsulation
        self.posts = []
        User.total_users += 1

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.like_post(self)

    # Class method: creates a guest user with a random username
    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        username = "guest" + str(random_number)
        display_name = "Guest"
        return cls(username, display_name, password="guest123")

    # Encapsulation methods for password
    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password



# post.py
class Post:
    total_posts = 0  # Class attribute to track total posts

    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []          # Public list of users who liked the post
        self._like_count = 0     # Private attribute for encapsulation
        Post.total_posts += 1

    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    def get_like_count(self):
        return self._like_count  # Safe access to like count

    # Static method: validate content length (up to 280 characters)
    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280



# socialnetwork.py
class SocialNetwork:
    def __init__(self):
        self.users = []  # List to store User objects
        self.posts = []  # List to store Post objects

    def add_user(self, user):
        if self.search_user_by_username(user.username):
            print("\nUser with username", user.username, "already exists!\n")
        else:
            self.users.append(user)
            print(user.display_name, "has been added to Chirpy.")

    def add_post(self, post):
        self.posts.append(post)
        print("A new post has been added to Chirpy.")

    def search_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def remove_user(self, username):
        user_to_remove = self.search_user_by_username(username)
        if user_to_remove:
            self.users.remove(user_to_remove)
            print("\n", user_to_remove.display_name, "has been removed from Chirpy.")
        else:
            print("\nUser with username", username, "not found!")

    def list_all_posts(self):
        if not self.posts:
            print("\nNo posts to display.")
        else:
            for post in self.posts:
                print(post.author.display_name + " posted: '" + post.content + "'")

    # Search posts by keyword
    def search_post_by_keyword(self, keyword):
        matching_posts = []
        for post in self.posts:
            if keyword.lower() in post.content.lower():
                matching_posts.append(post)
        return matching_posts



# main.py
from user import User
from post import Post
from social_network import SocialNetwork

# Create the SocialNetwork instance
chirpy_network = SocialNetwork()

# Create users
user1 = User("alex123", "Alex", "secret123")
user2 = User("emma456", "Emma", "password456")
guest = User.create_guest_user()

# Add users to the network
chirpy_network.add_user(user1)
chirpy_network.add_user(user2)
chirpy_network.add_user(guest)

# Attempt to add a duplicate user
chirpy_network.add_user(User("alex123", "Alex Duplicate", "pass"))

# Users create posts
post1 = user1.create_post("Hello world! This is my first chirp on Chirpy.")
post2 = user2.create_post("Excited to join Chirpy!")
post3 = guest.create_post("I'm a guest user posting a chirp!")

# Add posts to the network
chirpy_network.add_post(post1)
chirpy_network.add_post(post2)
chirpy_network.add_post(post3)

# List all posts
print("\nAll Posts in Chirpy:")
chirpy_network.list_all_posts()

# Search for a user
found_user = chirpy_network.search_user_by_username("alex123")
if found_user:
    print("\nFound user:", found_user.display_name)

# Remove a user
chirpy_network.remove_user("emma456")

# Search posts by keyword
keyword = "chirp"
matching_posts = chirpy_network.search_post_by_keyword(keyword)
print("\nPosts containing keyword '{}':".format(keyword))
for post in matching_posts:
    print("{} posted: '{}'".format(post.author.display_name, post.content))

# Test password encapsulation
print("\nPassword check for Alex:", user1.check_password("secret123"))  # True
user1.change_password("newSecret123")
print("Password check after change:", user1.check_password("newSecret123"))  # True

# Test post like system
user1.like_post(post2)   # Alex likes Emma's post
guest.like_post(post1)   # Guest likes Alex's post
print("\nLikes on Alex's post:", post1.get_like_count())
print("Likes on Emma's post:", post2.get_like_count())

