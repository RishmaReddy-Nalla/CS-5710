def print_star_pattern():
    # Number of rows for the pattern
    rows = 7
    
    for i in range(1, rows + 1):
        # Print stars for the first part of the pattern
        for j in range(1, i + 1):
            print("*", end=" ")
        
        # New line after each row
        print()
    
    for i in range(rows, 0, -1):
        # Print stars for the second part of the pattern
        for j in range(1, i):
            print("*", end=" ")
        
        # New line after each row
        print()

# Call the function to print the pattern
print_star_pattern()
