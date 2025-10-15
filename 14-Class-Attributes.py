# These codes are actually 3 seperate file codes but we will keep them here for learning. if u run them, then make 3 files.
# Files are named below:


# main.py
from user import User
from post import Post

# Create users
user1 = User("alex123", "Alex")
user2 = User("emma456", "Emma")

# Users create posts using instance methods
post1 = user1.create_post("Hello world! This is my first chirp.")
post2 = user2.create_post("Excited to join Chirpy!")

# Display posts
print(user1.display_name + " posted: '" + post1.content + "'")
print(user2.display_name + " posted: '" + post2.content + "'")

# Users interact with posts
user2.like_post(post1)
user1.like_post(post2)

# Display class-level totals
print("Total users on Chirpy:", User.total_users)
print("Total posts on Chirpy:", Post.total_posts)




# Post.py
class Post:
    total_posts = 0  # Class attribute
  
    def __init__(self, content, author):
        self.content = content  
        self.author = author 
        self.likes = [ ]  
        Post.total_posts += 1 # Adds total posts to the Post class
    
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")




# User.py
from post import Post  # Import the Post class

class User:
    max_posts = 5  # Class attribute that limits the number of posts a user can make

    def __init__(self, username, display_name):
        self.username = username
        self.display_name = display_name
        self.posts = [ ]  # List of posts created by the user
        self.posts_count = 0  # Track the number of posts created by the user

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    def create_post(self, content):
        if self.posts_count < User.max_posts:  # Check if user has exceeded post limit
            post = Post(content, self)
            self.posts.append(post)
            self.posts_count += 1  # Increment the post count
            print(self.display_name + " created a new post: '" + content + "'")
            return post
        else:
            print(self.display_name + " has reached the maximum post limit of " + str(User.max_posts) + " posts.")