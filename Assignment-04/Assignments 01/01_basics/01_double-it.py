def main():
    curr_value = int(input("Enter a number: "))  # Get user input as an integer

    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print the doubled value in the same line

# Run the function
if __name__ == '__main__':
    main()
