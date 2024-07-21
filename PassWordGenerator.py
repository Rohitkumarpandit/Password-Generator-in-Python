import random
import string

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
      length: The desired length of the password.

  Returns:
      A randomly generated password string.
  """
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  all_characters = lowercase + uppercase + digits + punctuation


  password = ''.join(random.sample(lowercase, 1) + random.sample(uppercase, 1) +
                     random.sample(digits, 1) + random.sample(punctuation, 1))

  
  password += ''.join(random.choices(all_characters, k=length - 4))
  return password

# Get password length from user
while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length >= 8:
      break
    else:
      print("Password length must be at least 8 characters. Please try again.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Generate and print the password
password = generate_password(length)
print(f"Your generated password is: {password}")