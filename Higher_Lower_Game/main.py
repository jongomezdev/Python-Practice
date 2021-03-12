#Display ASCII art

from art import logo
from game_data import data
import random
print(logo)

# Generate random IG accounts from list

account_a = random.choice(data)
account_b = random.choice(data)
#conditional to check if accounts are the same, if so make them different
if account_a == account_b:
  account_b = random.choice(data)

# Format the account data when printed

account_name = account_a["name"]
account_desc = account_a["description"]
account_country = account_a["country"]

# Ask the user for a guess

# Check answer is correct
  # Check follower count
      # Use if statement

# Give user feedback on their guess

# score keeping

# Make the game repeatable using a while loop

# Make the guess move up to the top position and set up comparison for the next account

# clear screen between rounds