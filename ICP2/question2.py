my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through the list and print elements at odd indexes
for index in range(len(my_list)):
    if index % 2 != 0:
        print(my_list[index])
