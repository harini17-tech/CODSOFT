import random
import string
print("===== Simple Password Generator =====")
length = int(input("Enter the desired password length: "))
print("\nChoose password complexity:")
print("1. Only letters (a-z, A-Z)")
print("2. Letters and numbers (a-z, A-Z, 0-9)")
print("3. Letters, numbers, and symbols (a-z, A-Z, 0-9, !@#$ etc.)")
choice = input("Enter your choice (1/2/3): ")
if choice == '1':
    characters = string.ascii_letters  
elif choice == '2':
    characters = string.ascii_letters + string.digits 
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation 
else:
    print("Invalid! Please add Special characters.")
    characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
print(f"\nYour generated password is:{password}")
