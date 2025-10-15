
fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
list_daily_steps = []
length_list = len(fitness_data)
list_daily_steps = fitness_data[1:length_list]
print(list_daily_steps)


# u can use below code for same solution


fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
list_daily_steps = fitness_data[1:len(fitness_data)]
print(list_daily_steps)



#  Your putting index value of 1 to 7 from fitness_data into list_daily_steps list.

# You could have literally left len() function and just did list_daily_steps = fitness_data[1:7] as this list was very less populated. so it would be:

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
list_daily_steps = fitness_data[1:7]
print(list_daily_steps)

#  You did len() to calculate total number in advance as on industrial scale, you work with bigger data than this. 
