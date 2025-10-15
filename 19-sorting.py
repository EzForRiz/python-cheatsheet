def sort_list(unsorted_list):
  sorted_list = []
  
  min_value = min(unsorted_list)  # Find the smallest number
  sorted_list.append(min_value)   # Add that number to new list
  return sorted_list

steps = [4, 2, 8]
sorted_steps = sort_list(steps)
print(sorted_steps)

# This one only finds one smallest number and stops. output is 2.
# It doesn’t sort the full list — just picks the smallest once.





def sort_list(unsorted_list):
  sorted_list = []
  for i in range(len(unsorted_list)):   # Repeat for every item
    min_value = min(unsorted_list)
    sorted_list.append(min_value)
  return sorted_list

# This one tries to sort, but forgets to remove the number it already used.





def sort_list(unsorted_list):
  sorted_list = []
  for i in range(len(unsorted_list)):
    min_value = min(unsorted_list)     # Find smallest
    sorted_list.append(min_value)      # Add it to sorted list
    unsorted_list.remove(min_value)    # Remove it from original
  return sorted_list

# Now it works properly!
# Each time, it finds the smallest number, moves it, and removes it.
# [2, 4, 8] is output