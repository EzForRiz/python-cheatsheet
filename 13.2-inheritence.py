# Inheritance in object-oriented programming (OOP) is a mechanism that allows a new class to acquire the properties and behaviors of an existing class, creating a hierarchical relationship and enabling code reuse. The new class, called a derived class or child class, inherits from the base class or parent class, gaining its functionalities and optionally adding its own.



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
# Chirpy Social Network - All-in-One File
# Demonstrates OOP concepts: Inheritance, Encapsulation, Polymorphism
# =====================================================

import random  # Needed for guest user creation

# =====================================================
# Comment Class
# =====================================================
class Comment:
    def __init__(self, text, commenter):
        self._text = text               # Private text of the comment
        self._commenter = commenter     # Private reference to User object

    def __str__(self):
        return f"{self._commenter.display_name} commented: '{self._text}'"  # User-friendly display

# =====================================================
# Post Class
# =====================================================
class Post:
    total_posts = 0  # Class variable to track total posts

    def __init__(self, content, author):
        self._content = content       # Private content of post
        self._author = author         # Private User object who authored post
        self._likes = []              # Private list of Users who liked the post
        self._like_count = 0          # Private counter for likes
        self._comments = []           # Private list of Comment objects
        Post.total_posts += 1         # Increment total posts

    @property
    def content(self):
        return self._content          # Getter for post content

    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")  # Validate content length
        self._content = new_content   # Update content

    @property
    def author(self):
        return self._author           # Read-only property for author

    def like_post(self, user):
        if user not in self._likes:   # Check if user already liked
            self._likes.append(user)  # Add to likes
            self._like_count += 1     # Increment like count
            print(user.display_name, "liked this post!")  # Feedback
        else:
            print(user.display_name, "has already liked this post!")  # Already liked

    def get_like_count(self):
        return self._like_count       # Return total likes

    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)  # Create comment object
        self._comments.append(comment)      # Add comment to list
        print(comment._commenter.display_name, "added a comment on", self._author.display_name + "'s post.")  # Feedback
        return comment                       # Return the Comment object

    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280           # Validate max length of content

    def __repr__(self):
        snippet = self._content if len(self._content) <= 30 else self._content[:27] + "..."  # Snippet for debugging
        return f"<Post by {self._author.username}: '{snippet}', Likes: {self._like_count}'>"

# =====================================================
# User Class
# =====================================================
class User:
    total_users = 0  # Class variable to track total users

    def __init__(self, username, display_name, password):
        self._username = username      # Private username
        self._display_name = display_name  # Private display name
        self._password = password      # Private password
        self._posts = []               # Private list of posts
        User.total_users += 1          # Increment total users

    @property
    def username(self):
        return self._username          # Read-only username

    @property
    def display_name(self):
        return self._display_name      # Getter for display name

    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")  # Validate non-empty
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")  # Validate length
        self._display_name = value     # Update display name

    def show_profile(self):
        print("User:", self._display_name, "(@" + self._username + ")")  # Show profile info

    def create_post(self, content):
        post = Post(content, self)     # Create new Post object
        self._posts.append(post)       # Add post to user's posts
        return post                    # Return the Post

    def like_post(self, post):
        post.like_post(self)           # Like a post

    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)  # Generate random number
        guest_username = "guest" + str(random_number)  # Generate guest username
        return cls(guest_username, "Guest", "guestpass")  # Return guest User object

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password  # Update password
            print("Password updated successfully!")  # Feedback
        else:
            print("Error: Password must be at least 6 characters long.")  # Invalid

    def check_password(self, input_password):
        return input_password == self._password  # Check password correctness

    def __str__(self):
        return f"<User: {self._display_name} ({self._username})>"  # Friendly string

# =====================================================
# VerifiedUser Class
# =====================================================
class VerifiedUser(User):
    def __init__(self, username, display_name, password):
        super().__init__(username, display_name, password)  # Call parent constructor
        self._verification_badge = True                     # Private badge
        self._display_name = "✅ " + display_name           # Add badge to display name

    def get_verification_status(self):
        return "Verified ✅" if self._verification_badge else "Regular"  # Return verification status

    def create_post(self, content):
        verified_content = "✅ " + content  # Add verified flair
        post = Post(verified_content, self) # Create post object
        self._posts.append(post)            # Add to user's posts
        return post

# =====================================================
# AdminUser Class
# =====================================================
class AdminUser(User):
    def delete_post(self, post, posts_list):
        if post in posts_list:
            posts_list.remove(post)                   # Remove post from list
            print(f"Admin {self.display_name} has deleted the post: {post.content}")  # Feedback
        else:
            print("Post not found. Unable to delete.")  # Error if post not found

# =====================================================
# SocialNetwork Class
# =====================================================
class SocialNetwork:
    def __init__(self):
        self._users = []  # Private list of users
        self._posts = []  # Private list of posts

    def add_user(self, user, verified):
        username = user.username                  # Extract username
        display_name = user.display_name         # Extract display name
        password = user._password                 # Extract password

        if self.search_user_by_username(username):  # Check for duplicate user
            print(f"\nUser with username '{username}' already exists!\n")
            return

        if verified == "yes":                     # Create verified or regular user
            new_user = VerifiedUser(username, display_name, password)
        else:
            new_user = User(username, display_name, password)

        self._users.append(new_user)              # Add user to network
        print(display_name, "has been added to Chirpy.")  # Feedback

    def add_post(self, post):
        self._posts.append(post)                  # Add post to network
        print("A new post has been added to Chirpy.")  # Feedback

    def search_user_by_username(self, username):
        for user in self._users:
            if user.username == username:        # Match username
                return user
        return None                               # Not found

    def list_all_posts(self):
        if not self._posts:
            print("\nNo posts to display.")      # Empty check
        else:
            for index, post in enumerate(self._posts):
                print(index, ". ", post.author.display_name, " posted: '", post.content, "'", sep="")
                if post._likes:                  # Show likes
                    liked_by = ", ".join(user.display_name for user in post._likes)
                    print("   Liked by:", liked_by)
                if post._comments:               # Show comments
                    for comment in post._comments:
                        print("     - ", comment._commenter.display_name, ": '", comment._text, "'", sep="")

# =====================================================
# Main Menu System
# =====================================================
_chirpy_network = SocialNetwork()  # Initialize network

def display_menu():
    print("\n Chirpy Social Media Platform")  # Header
    print("========================================")
    print("1. Create New Account")
    print("2. Post a Chirp")
    print("3. View All Chirps")
    print("4. Like a Chirp")
    print("5. Comment on a Chirp")
    print("6. View Profile")
    print("7. List All Users")
    print("8. Exit")

def create_account():
    username = input("Enter username: ")       # Prompt username
    display_name = input("Enter display name: ")  # Prompt display name
    password = input("Enter password: ")       # Prompt password
    verified = input("Do you want a verified account? (yes/no): ").strip().lower()  # Prompt verification
    if verified == "yes":
        user = VerifiedUser(username, display_name, password)  # Create verified user
    else:
        user = User(username, display_name, password)          # Create regular user
    _chirpy_network.add_user(user, verified)                    # Add user to network
    print(f"Account created successfully for {display_name}!") # Feedback

def post_chirp():
    username = input("Enter your username: ")                  # Prompt username
    user = _chirpy_network.search_user_by_username(username)   # Find user
    if user:
        content = input("Enter your chirp: ")                  # Prompt content
        post = user.create_post(content)                       # Create post
        _chirpy_network.add_post(post)                         # Add to network
    else:
        print("User not found.")

def view_chirps():
    _chirpy_network.list_all_posts()                            # Show all posts

def like_chirp():
    username = input("Enter your username: ")                  # Prompt username
    user = _chirpy_network.search_user_by_username(username)   # Find user
    if user:
        _chirpy_network.list_all_posts()                       # Show posts
        try:
            post_index = int(input("Enter post index to like: "))  # Prompt post index
            if 0 <= post_index < len(_chirpy_network._posts):
                user.like_post(_chirpy_network._posts[post_index])  # Like post
            else:
                print("Invalid post index.")                   # Invalid index
        except ValueError:
            print("Invalid input. Please enter a number.")     # Invalid input
    else:
        print("User not found.")

def comment_on_chirp():
    username = input("Enter your username: ")                  # Prompt username
    user = _chirpy_network.search_user_by_username(username)   # Find user
    if user:
        _chirpy_network.list_all_posts()                       # Show posts
        try:
            post_index = int(input("Enter post index to comment on: "))  # Prompt post index
            if 0 <= post_index < len(_chirpy_network._posts):
                comment = input("Enter your comment: ")       # Prompt comment
                _chirpy_network._posts[post_index].add_comment(comment, user)  # Add comment
            else:
                print("Invalid post index.")                   # Invalid index
        except ValueError:
            print("Invalid input. Please enter a number.")     # Invalid input
    else:
        print("User not found.")

def view_profile():
    username = input("Enter username to view profile: ")       # Prompt username
    user = _chirpy_network.search_user_by_username(username)   # Find user
    if user:
        user.show_profile()                                    # Show profile
    else:
        print("User not found.")

def list_users():
    if _chirpy_network._users:
        print("\nRegistered Users:")
        for user in _chirpy_network._users:                   # List all users
            print(user)
    else:
        print("No users registered yet.")

# Main loop
while True:
    display_menu()                                              # Show menu
    choice = input("Choose an option (1-8): ").strip()         # Prompt choice
    
    if choice == "1":
        create_account()                                        # Option 1
    elif choice == "2":
        post_chirp()                                            # Option 2
    elif choice == "3":
        view_chirps()                                           # Option 3
    elif choice == "4":
        like_chirp()                                            # Option 4
    elif choice == "5":
        comment_on_chirp()                                      # Option 5
    elif choice == "6":
        view_profile()                                          # Option 6
    elif choice == "7":
        list_users()                                            # Option 7
    elif choice == "8":
        print("Exiting Chirpy. Goodbye!")                      # Exit
        break
    else:
        print("Invalid choice. Try again.")                     # Invalid option









# the code below is for understanding. choose whichever u like more.






# =====================================================
# Chirpy Social Network - All-in-One File 
# Demonstrates OOP concepts: Inheritance, Encapsulation, Polymorphism
# =====================================================

# =====================================================
# User Class
# =====================================================
from post import Post  
import random

class User:
    total_users = 0  

    def __init__(self, username, display_name, password):
        self._username = username
        self._display_name = display_name  # Private attribute
        self._password = password          # Private attribute
        self._posts = [ ]                   # Private attribute for user posts
        User.total_users += 1

    # Read-only property for username (since it shouldn't change after creation)
    @property
    def username(self):
        return self._username

    # Getter for display_name
    @property
    def display_name(self):
        return self._display_name

    # Setter for display_name
    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")
        self._display_name = value

    def show_profile(self):
        print("User:", self._display_name, "(@" + self._username + ")")

    def create_post(self, content):
        post = Post(content, self)
        self._posts.append(post)
        return post

    def like_post(self, post):
        post.like_post(self)

    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        guest_username = "guest" + str(random_number)
        guest_display_name = "Guest"
        return cls(guest_username, guest_display_name, "guestpass")

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password
    
    # Provide a user-friendly string representation
    def __str__(self):
        return "<User: %s (%s)>" % (self._display_name, self._username)




# =====================================================
# Post Class
# =====================================================
from comment import Comment  

class Post:
    total_posts = 0

    def __init__(self, content, author):
        self._content = content   # Private attribute for content
        self._author = author     # Private attribute for author
        self._likes = []          # Private attribute for users who liked the post
        self._like_count = 0      # Private attribute for counting likes
        self._comments = [ ]       # Private attribute for storing comments
        Post.total_posts += 1

    # Getter for content
    @property
    def content(self):
        return self._content

    # Setter for content with validation
    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")
        self._content = new_content

    # Read-only property for author
    @property
    def author(self):
        return self._author

    def like_post(self, user):
        if user not in self._likes:
            self._likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    def get_like_count(self):
        return self._like_count

    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)
        self._comments.append(comment)
        print(comment._commenter.display_name, "added a comment on", self._author.display_name + "'s post.")
        return comment

    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280

    def __repr__(self):
        # Show a snippet if content is over 30 characters
        snippet = self._content if len(self._content) <= 30 else self._content[:27] + "..."
        return "<Post by " + self._author.username + ": '" + snippet + "', Likes: " + str(self._like_count) + ">"




# =====================================================
# Comment Class
# =====================================================
class Comment:
    def __init__(self, text, commenter):
        self._text = text          # The text content of the comment
        self._commenter = commenter  # The User who made the comment

    def __str__(self):
        return self._commenter.display_name + " commented: '" + self._text + "'"




# =====================================================
# SocialNetwork Class
# =====================================================
from user import User
from verified_user import VerifiedUser

class SocialNetwork:
    def __init__(self):
        self._users = [ ]  # Private list to store User objects
        self._posts = [ ]  # Private list to store Post objects

    def add_user(self, user, verified):
        account_type = verified

        # Extract user information
        username = user.username
        display_name = user.display_name
        password = user._password

        # Check if user already exists
        if self.search_user_by_username(username):
            print("\nUser with username '{}' already exists!\n".format(username))
            return

        # Create the appropriate user object
        if account_type == "True":
            new_user = VerifiedUser(username, display_name, password)
        else:
            new_user = User(username, display_name, password)

        # Add the new user to the network
        self._users.append(new_user)
        print(display_name, "has been added to Chirpy.")

    def add_post(self, post):
        self._posts.append(post)
        print("A new post has been added to Chirpy.")

    def search_user_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None

    def search_user_for_post(self, username, password):
        user = self.search_user_by_username(username)
        if user:
            if user.check_password(password):
                return user
            else:
                print("Enter correct password.")
        else:
            print("User not found.")
        return None

    def remove_user(self, username):
        user_to_remove = self.search_user_by_username(username)
        if user_to_remove:
            self._users.remove(user_to_remove)
            print("\n", user_to_remove.display_name, "has been removed from the Chirpy.")
        else:
            print("\nUser with username", username, "not found!")

    def list_all_posts(self):
        if not self._posts:
            print("\nNo posts to display.")
        else:
            for index, post in enumerate(self._posts):  # Add index using enumerate
                print(index, ". ", post.author.display_name, " posted: '", post.content, "'", sep="")

                # Show likes if any
                if post._likes:
                    liked_by = ", ".join(user.display_name for user in post._likes)
                    print("   Liked by:", liked_by)

                # Show comments if any
                if post._comments:
                    for comment in post._comments:
                        print("     - ", comment._commenter.display_name, ": '", comment._text, "'", sep="")



# =====================================================
# VerifiedUser Class (inherits User)
# =====================================================
from user import User
from post import Post

class VerifiedUser(User):
    def __init__(self, username, display_name, password):
        # Initialize using User's constructor
        super().__init__(username, display_name, password)
        # Privately mark the user as verified
        self._verification_badge = True
        # Update the private display name attribute to include a verified badge
        self._display_name = "✅ " + display_name

    def get_verification_status(self):
        return "Verified ✅" if self._verification_badge else "Regular"

    # Override create_post() to include verified flair in post content
    def create_post(self, content):
        verified_content = "✅ " + content
        post = Post(verified_content, self)
        self._posts.append(post)
        return post




# =====================================================
# AdminUser Class (inherits User)
# =====================================================
class AdminUser(User):
    def __init__(self, username, display_name, password):
        super().__init__(username, display_name, password)

    # Delete a post from a list
    def delete_post(self, post, posts_list):
        if post in posts_list:
            posts_list.remove(post)
            print(f"Admin {self.display_name} has deleted the post: {post.content}")
        else:
            print("Post not found. Unable to delete.")






# =====================================================
# Main.py
# =====================================================
from social_network import SocialNetwork
from user import User
from verified_user import VerifiedUser

# Initialize the Chirpy Social Network
_chirpy_network = SocialNetwork()

def display_menu():
    print("\n Chirpy Social Media Platform")
    print("========================================")
    print("1. Create New Account")
    print("2. Post a Chirp")
    print("3. View All Chirps")
    print("4. Like a Chirp")
    print("5. Comment on a Chirp")
    print("6. View Profile")
    print("7. List All Users")
    print("8. Exit")

def create_account():
    username = input("Enter username: ")
    display_name = input("Enter display name: ")
    password = input("Enter password: ")
    verified = input("Do you want a verified account? (yes/no): ").strip().lower()
    if verified == "yes":
        user = VerifiedUser(username, display_name, password)
    else:
        user = User(username, display_name, password)
    _chirpy_network.add_user(user, verified)
    print(f"Account created successfully for {display_name}!")

def post_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        content = input("Enter your chirp: ")
        post = user.create_post(content)
        _chirpy_network.add_post(post)
    else:
        print("User not found.")

def view_chirps():
    _chirpy_network.list_all_posts()

def like_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to like: "))
            if 0 <= post_index < len(_chirpy_network._posts):
                user.like_post(_chirpy_network._posts[post_index])
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")

def comment_on_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to comment on: "))
            if 0 <= post_index < len(_chirpy_network._posts):
                comment = input("Enter your comment: ")
                _chirpy_network._posts[post_index].add_comment(comment, user)
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")

def view_profile():
    username = input("Enter username to view profile: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        user.show_profile()
    else:
        print("User not found.")

def list_users():
    if _chirpy_network._users:
        print("\nRegistered Users:")
        for user in _chirpy_network._users:
            print(user)
    else:
        print("No users registered yet.")

while True:
    display_menu()
    choice = input("Choose an option (1-8): ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        post_chirp()
    elif choice == "3":
        view_chirps()
    elif choice == "4":
        like_chirp()
    elif choice == "5":
        comment_on_chirp()
    elif choice == "6":
        view_profile()
    elif choice == "7":
        list_users()
    elif choice == "8":
        print("Exiting Chirpy. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")