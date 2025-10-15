# ------------------ PIE CHART ------------------

from matplotlib import pyplot

data = [3, 4, 5]    # These are the three slices of our pie chart

pyplot.pie(data)   # This line creates a simple pie chart based on the numbers above




# ------------------ PIE CHART WITH COLORS & LABELS ------------------

from matplotlib import pyplot

# The numbers show how big each slice is
data = [1, 6, 3]

# These are the colors of the slices
zones = ["green", "orange", "red"]

# These are the labels that will appear on each slice
zone_labels = ["Excellent", "Fine", "Concerning"]

# This line draws the pie chart with colors, labels, and percentage values
pyplot.pie(data, colors=zones, labels=zone_labels, autopct='%.0f%%')




# ------------------ BASIC BAR CHART ------------------

from matplotlib import pyplot

# Data we want to show (step counts or any other values)
data = [3, 4, 5]

# Positions of each bar on the x-axis
x_axis = [1, 2, 3]

# Draw the bar chart
pyplot.bar(x_axis, data)




# ------------------ BAR CHART WITH TEXT LABELS ------------------

from matplotlib import pyplot

# Same data, but now we’ll use words instead of numbers on the x-axis
data = [3, 4, 5]
x_axis = ["a", "b", "c"]

# Each bar will have a label under it instead of a number
pyplot.bar(x_axis, data)




# ------------------ SCATTER PLOT ------------------

from matplotlib import pyplot

# Each point represents one day
x_values = [1, 2, 3, 4, 5, 6, 7]  # Day numbers
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]  # Steps taken each day

# Plot individual points on a graph
pyplot.scatter(x_values, y_values)




# ------------------ LINE PLOT ------------------

from matplotlib import pyplot

# Same data as above, but now we’ll connect the dots with lines
x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]

# Draw a line through all the points to show progress over time
pyplot.plot(x_values, y_values)




# ------------------ BUBBLE PLOT ------------------

from matplotlib import pyplot

# Just like a scatter plot, but bubble sizes show an extra piece of info
x_values = [1, 2, 3, 4, 5, 6, 7]        # Day numbers
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]  # Steps
weight = [100, 150, 2000, 200, 400, 300, 250]            # Bubble sizes

# The "weight" decides how big each bubble will appear
pyplot.scatter(x_values, y_values, weight)




# ------------------ BAR CHART USING CSV FILE ------------------

# Make sure you have a file named "data_steps.csv" with this data inside:
# Day,Steps
# Sunday,3000
# Monday,6000
# Tuesday,7000
# Wednesday,8000
# Thursday,9000
# Friday,10000
# Saturday,9500

from matplotlib import pyplot as plt
import numpy as np

# Load the data from the CSV file
# skiprows=1 means "ignore the first row" (because it's just headers)
data = np.loadtxt('data_steps.csv', delimiter=',', dtype=str, skiprows=1)

# Separate the two columns into 'days' and 'steps'
days = data[:, 0]               # First column = day names
steps = data[:, 1].astype(int)  # Second column = step numbers (turned into integers)

# Draw a bar chart with days on the x-axis and steps on the y-axis
plt.bar(days, steps, color='skyblue')

# Add a title and labels so the graph is easy to read
plt.title('Weekly Step Count')   # Chart title
plt.xlabel('Days of the Week')   # X-axis label
plt.ylabel('Steps')              # Y-axis label

# Finally, show the chart
plt.show()




#you can use this too for a bar plot, but only if your CSV file is structured horizontally — meaning the days and steps are stored in rows, not columns.:

from matplotlib import pyplot
import numpy

data = numpy.loadtxt('daily_steps.csv', delimiter = ',', dtype = str)

days = data[0] # Reading the 0th row as an array of strings, days of the week 
steps = data[1] # Reading the next row as the steps
steps = steps.astype(int) # Converting the steps to an array of integers

pyplot.bar(days, steps) # Finally, plotting the days on the x-axis and steps on the y-axis