import getpass
import string

long_enough = None
found_pass = False

print("Hello There this is a CLI Password checker in my book a good password is at least 12 characters long, has uppercases, lowercase letters, symbols, and numbers lets see if yours is good enough :) ")

print("Type in your password: ")

password = getpass.getpass()

uppercase = any([char in string.ascii_uppercase for char in password])
lowercase = any([char in string.ascii_lowercase for char in password])
digits = any([char in string.digits for char in password])
punctuation = any([char in string.punctuation for char in password])
pass_length = len(password)

try:
    with open('10k-most-common.txt', 'r') as f:
        for line in f:
            if password.strip() == line.strip():
                found_pass = True
                break
except FileNotFoundError:
    print("Warning: Common password list not found.")
    found_pass = False

long_enough = pass_length >= 12

print(f"Has uppercases? {uppercase}")
print(f"Has lowercases? {lowercase}")
print(f"Has digits? {digits}")
print(f"Has punctuation? {punctuation}")
print(f"Has adequate length? {long_enough}")
print(f"found password in common password file? {found_pass}")


good_password = uppercase and lowercase and digits and punctuation and long_enough
if found_pass == True and good_password == True:
    good_password = False
print(f"is your password Strong? {good_password}")
print("Thanks for checking this tool out ;) ")