import random

# Ask the user to choose heads (1) or tails (0)
user_choice = int(input("What do you choose? Type 0 for tail, 1 for head: "))

# Generate a random integer (0 or 1) to represent the coin toss result
rand_integer = random.randint(0, 1)

# Check if the user's choice matches the random result
if user_choice == rand_integer:
    print("You win!")
else:
    print("You lose.")
