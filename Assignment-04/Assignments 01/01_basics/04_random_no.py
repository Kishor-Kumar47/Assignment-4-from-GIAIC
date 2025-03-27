import random  # Import the random module

def main():
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100), end=" ")  # Generate and print a random number

# Run the function
if __name__ == '__main__':
    main()
