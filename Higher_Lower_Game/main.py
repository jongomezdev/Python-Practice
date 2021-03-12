#Import 
from art import logo, vs
from game_data import data
import random


def format_data(account):
  # Create function for less repeated code 
  """Takes the account data and returns the printable format"""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, be_followers):
  """Use if statement to check if user is correct."""
  if a_followers > be_followers:
    return guess == "a"
  else:
    return guess == "b"


#Display ASCII art
print(logo)

# Generate random IG accounts from list

account_a = random.choice(data)
account_b = random.choice(data)
#conditional to check if accounts are the same, if so make them different
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare B: {format_data(account_b)}.")

# Ask the user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check answer is correct
  # Check follower count
      # Use if statement

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]


# Give user feedback on their guess

# score keeping

# Make the game repeatable using a while loop

# Make the guess move up to the top position and set up comparison for the next account

# clear screen between rounds