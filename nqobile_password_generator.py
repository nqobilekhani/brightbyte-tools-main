# random password generator
# Generates a random password containing a mix of characters.

import sys
import random
import string

def generate_password(length=12):
    """
    Generates a random password containing a mix of characters.
    """

    # Define the sets of characters to use
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Ensure the length is a positive integer
    if length <= 0:
      return "Password length must be greater than 0."

    # Generate the password by randomly sampling from the character set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Added this comment
if len(sys.argv) < 2:
  print("-----This is a simple passowrd generator-----")
  size =int(input("Enter password length:  "))

else:
  size = int(sys.argv[1])
# Print the password to the screen
# password_12 = generate_password()
# print(f"12-Character Password: {password_12}")

new_password = generate_password(size)
print(f"Your new password is: {new_password}")