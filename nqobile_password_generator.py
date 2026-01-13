# random password generator
# Generates a random password containing a mix of characters.
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

# Print thye password to the screen
password_12 = generate_password()
print(f"12-Character Password: {password_12}")