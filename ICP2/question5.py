def count_case_characters(input_string):
    upper_case_count = 0
    lower_case_count = 0

    for char in input_string:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1

    return upper_case_count, lower_case_count

# Input String
input_string = 'The quick Brow Fox'

# Get the counts of upper-case and lower-case characters
upper_case_count, lower_case_count = count_case_characters(input_string)

# Print the results
print(f"No. of Upper-case characters: {upper_case_count}")
print(f"No. of Lower-case Characters: {lower_case_count}")
