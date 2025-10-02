import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # special characters

    # Combine all
    all_chars = letters + digits + symbols

    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining length with random choices
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))
