import numpy  # Importing the NumPy library to handle numerical data easily

# --- Loading one data element from file ---
data = numpy.loadtxt('data.txt')  # Loading a single numeric value from data.txt
print(data)  # Printing the single loaded value

# --- Loading two data values into two variables ---
num1, num2 = numpy.loadtxt('data.csv', delimiter=',')  # Loading two numeric values from data.csv into two variables
print(num1, num2)  # Printing both numbers

# --- Loading a list of values (like many numbers in one row) ---
data = numpy.loadtxt('data.txt', delimiter=',')  # Loading multiple numeric values (comma-separated) into a list (NumPy array)
print(len(data))  # Printing how many numbers are in the list

# --- Loading mixed data types (like names + numbers) ---
data = numpy.loadtxt('data.csv', dtype=str, delimiter=',')  # Reading all data as strings to handle names + step counts
print(data)  # Printing the mixed data as strings

# --- Challenge: converting string numbers to integers ---

name = data[0]  # Extracting the name from the first element
steps = data[1:]  # Extracting the step counts (still as strings)

# ✅ Solution 1: Using list comprehension (regular Python)
steps = [int(x) for x in steps]  # Converting all string step counts to integers
print(type(steps[0]))  # Checking the data type (should be <class 'int'>)

# ✅ Solution 2: Using NumPy’s built-in conversion (faster for big data)
data = numpy.loadtxt('data.csv', dtype=str, delimiter=',')  # Reloading data as strings again
name = data[0]  # Extracting the name again
steps = data[1:].astype(int)  # Converting string steps to integers using NumPy
print(type(steps[0]))  # Checking the data type (should be <class 'numpy.int64'>)
