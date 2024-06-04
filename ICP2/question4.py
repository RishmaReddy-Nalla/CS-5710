def get_unique_items(input_list):
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_list = list(set(input_list))
    return unique_list

# Sample List
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get Unique List
unique_list = get_unique_items(sample_list)

# Print the Unique List
print("Sample List:", sample_list)
print("Unique List:", unique_list)
