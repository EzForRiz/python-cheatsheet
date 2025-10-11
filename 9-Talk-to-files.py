with open("message.txt", "w") as file:
    file.write("Hello from Python!")

# You won’t see any output on the screen after running this code, and that’s normal! This code is writing the message “Hello from Python!” into a file called message.txt.

# The with open("message.txt", "w") part tells Python to open a file named message.txt in “write” mode ("w"). If the file doesn’t already exist, Python will create it for you. Once the file is open, file.write("Hello from Python!") writes the message to that file.




with open("message.txt", "r") as file:
    content = file.read()
    print(content)

# Read from a file





with open("message.txt", "a") as file:
    file.write("\nAnother line!")

# To Append (add) more content, Use mode "a" (append)





entry = input("Write a diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")

# Let's look at the code below that prompts the user for a diary entry and appends it to a file named diary.txt. The with open statement to handles the file operations, ensuring the file is properly closed after writing.





name = input("Please enter your name: ")
score = int(input("Enter your score: "))   #convert to integer

with open('PlayerScore.txt', 'w') as file:   #opens file in write mode.
    file.write(f"{name}, {score}\n")   

#   file.write() only accepts a single string. You can’t pass two arguments like:
#              file.write(name, score)
#   You need to convert the score to a string and format the output.





name = input("Player name: ")
score = input("Score: ")
# Gets input from the user

with open("PlayerScore.txt", "a") as file:
    file.write(name + ":" + score + "\n")
#  Opens the file in append mode ("a") and writes the data. If PlayerScore.txt doesn’t exist, it will be created. If it does exist, the new score is added at the end.
    
with open("PlayerScore.txt", "r") as file:
    content = file.read()
    print(content)
# Reads and displays all scores in the file.




# Key takeaway

# 'w' = overwrite / start fresh

# 'a' = append / keep adding

# Even if the file doesn’t exist yet, 'a' works perfectly—it will just create the file and start appending.
# Using 'w' also works if the file doesn’t exist, but it’s risky if you want to keep previous data.