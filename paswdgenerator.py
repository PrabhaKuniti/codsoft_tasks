import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    
    if length > 4:
        all_characters = lowercase + uppercase + digits + special
        password.extend(random.choice(all_characters) for _ in range(length - 4))
    
   
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
