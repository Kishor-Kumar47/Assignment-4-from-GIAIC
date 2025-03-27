import random

DONE_LIKELIHOOD = 0.3  # 30% chance of stopping early

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Stop counting early if done() returns True
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

# Run the main function
main()
