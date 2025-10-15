# ----------------------------
# Step 1: Import libraries
# ----------------------------
# numpy is used for array and numerical operations.
# matplotlib.pyplot is used for plotting graphs (line, bar, pie, etc.)
import numpy
from matplotlib import pyplot

# ----------------------------
# Step 2: Load CSV data
# ----------------------------
# The code loads a CSV file "steps.csv" with user step data.
# Each row represents a user: first column = name, next 168 columns = hourly steps.
# Initial exploration steps:
# - Print length of data to check number of rows
# - Print first element (header)
# - Print second element (first user data)
# These steps helped understand CSV structure before processing.
data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
print("Length of data =", len(data))
print("Data:\n", data)
print("First row (header):", data[0])
print("First user row:", data[1])

# ----------------------------
# Step 3: Convert data to dictionary
# ----------------------------
# Function data_to_dict transforms the 2D numpy array into a dictionary:
# - Key = user's name
# - Value = numpy array of 168 hourly steps
def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):  # skip header row
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict

# ----------------------------
# Step 4: Convert hourly to daily steps
# ----------------------------
# Function hourly_to_daily takes 168 hourly steps and sums every 24 hours to get 7 daily totals
def hourly_to_daily(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        daily_steps.append(sum(hourly_steps[i:i+24]))
    return daily_steps

# ----------------------------
# Step 5: Compute statistics
# ----------------------------
# compute_stats calculates min, max, average daily steps for each user
def compute_stats(step_dict):
    stats_dict = {}
    for key, value in step_dict.items():
        stats_dict[key] = {
            "min": min(value),
            "max": max(value),
            "average": numpy.mean(value)
        }
    return stats_dict

# ----------------------------
# Step 6: Categorize users
# ----------------------------
# choose_categories classifies users based on average daily steps:
# - <5000 steps → concerning
# - 5000–9999 steps → average
# - ≥10000 steps → excellent
def choose_categories(avg_list):
    categories = {"concerning":0, "average":0, "excellent":0}
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] += 1
        elif 5000 < avg_steps < 10000:
            categories["average"] += 1
        else:
            categories["excellent"] += 1
    return categories

# ----------------------------
# Step 7: Sum daily steps to weekly steps
# ----------------------------
def daily_to_total(daily_steps):
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict

# ----------------------------
# Step 8: Sorting users by steps
# ----------------------------
# Helper function find_min_index returns the index of the smallest element
def find_min_index(input_list):
    current_min = input_list[0]
    index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i
    return index

# my_sort sorts names and steps lists based on weekly steps (ascending)
def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")  # mark as used
    return sorted_user_names, sorted_user_steps

# ----------------------------
# Step 9: Plotting functions
# ----------------------------
# - plot_line → shows 24-hour steps for one user
# - plot_bar → shows weekly steps of all users as a bar chart
# - plot_pie → shows category distribution
# - plot_bubbles → optional, bubble chart for daily steps
# Note: save_path variable needs to be defined to save files
def plot_line(steps):
    hour_list = range(24)
    pyplot.title("Performance over the day")
    pyplot.xlabel("Hour of the day")
    pyplot.ylabel("Number of steps")
    pyplot.plot(hour_list, steps)
    pyplot.savefig(save_path+"plot4.png")
    pyplot.close()

def plot_pie(categories):
    pyplot.pie(categories.values(), labels=categories.items())
    pyplot.title("Pie chart for categories")
    pyplot.savefig(save_path+"plot3.png")
    pyplot.close()

def plot_bar(sorted_names, sorted_steps):
    pyplot.bar(sorted_names, sorted_steps)
    pyplot.xticks(rotation=45)
    pyplot.tight_layout()
    pyplot.savefig(save_path+"plot2.png")
    pyplot.close()

def plot_bubbles(daily_step_dict):
    # Placeholder for bubble plot
    pyplot.savefig(save_path+"plot1.png")
    pyplot.close()

# ----------------------------
# Step 10: Main execution
# ----------------------------
# This puts all the pieces together:
# 1. Load CSV → dictionary
# 2. Convert hourly → daily
# 3. Compute stats & categories
# 4. Sum daily → weekly steps
# 5. Sort users
# 6. Generate plots
def main():
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    avg_list = [stats_dict[name]["average"] for name in stats_dict]
    categories = choose_categories(avg_list)

    total_step_dict = daily_to_total(daily_step_dict)
    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    steps = data_dict["Juliana"][0:24]  # example user for line plot
    plot_line(steps)
    plot_pie(categories)
    plot_bar(sorted_names, sorted_steps)
    plot_bubbles(daily_step_dict)

main()
