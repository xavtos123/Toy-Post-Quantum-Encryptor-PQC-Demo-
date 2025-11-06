# Toy Post-Quantum Encryptor - Like a magic box that locks secrets so quantum computers can't break it!
# We use simple math (numbers like a puzzle) to scramble, then unscramble. No real quantum, just pretend safe lock.

import random  # Dice for the 'maze' numbers.
import string  # Alphabet for letters in messages.

def generate_lattice_key(size=5):
    # Creates a 'lattice' key - a grid of random numbers like a maze wall.
    # can be thought of as a 5x5 puzzle board with random walls (numbers 0-9).
    key = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
    return key

def encrypt_message(message, key):
    # Lock the message: Add maze numbers to each letter's code (A=1, B=2, etc.).
    encrypted = ""
    for char in message.upper():
        if char in string.ascii_uppercase:
            # Q = letter number (A=1 to Z=26).
            q = ord(char) - ord('A') + 1
            # Pick a random maze number from key (like choosing a wall height).
            maze_num = random.choice([row[random.randint(0, len(key)-1)] for row in key])
            # Lock: Q + maze_num, mod 26 (wrap around alphabet).
            locked = (q + maze_num) % 26
            if locked == 0:
                locked = 26  # No zero, back to Z.
            encrypted += chr(ord('A') + locked - 1)  # Back to letter.
        else:
            encrypted += char  # Keep spaces/symbols.
    return encrypted

def decrypt_message(encrypted, key):
    # Unlock: Subtract maze number from locked letter.
    decrypted = ""
    for char in encrypted.upper():
        if char in string.ascii_uppercase:
            locked = ord(char) - ord('A') + 1
            maze_num = random.choice([row[random.randint(0, len(key)-1)] for row in key])  # Same maze, different spot.
            q = (locked - maze_num) % 26
            if q == 0:
                q = 26
            decrypted += chr(ord('A') + q - 1)
        else:
            decrypted += char
    return decrypted

# Pretend space message.
secret_message = "Launch at noon"
key = generate_lattice_key()  # Make the magic maze.
locked = encrypt_message(secret_message, key)
unlocked = decrypt_message(locked, key)

print(f"Secret: {secret_message}")
print(f"Locked (Quantum-Safe): {locked}")
print(f"Unlocked: {unlocked}")
