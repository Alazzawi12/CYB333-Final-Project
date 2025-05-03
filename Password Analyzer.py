import os
import re
import string

# Load common passwords from file
def load_common_words(filepath="/Users/adamalazzawi/Desktop/Final Project/10-million-password-list-top-100000.txt"):
# This function loads a list of common passwords from a file and returns them as a set.    
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return set(line.strip().lower() for line in f if line.strip())
# Exception handling for file not found or other issues
    except FileNotFoundError:
        print(f"\n[!] Common passwords file not found at:\n   {filepath}")
        return set()

# Check if the password contains common words or patterns
def contains_common_word(password, common_words):
    lower_password = password.lower()
    for word in common_words:
        if word in lower_password:
            return True, word
    return False, None

# Check for sequential characters or patterns
def is_sequential(password):
    sequences = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password:
                return True
    return False

# Check for keyboard patterns
def is_keyboard_pattern(password):
    patterns = ['qwerty', 'asdfgh', 'zxcvbn', '123456']
    for pattern in patterns:
        if pattern in password.lower():
            return True
    return False

# Evaluate password strength
def evaluate_password_strength(password, common_words):
    suggestions = []
    score = 5

    # Check password length
    if len(password) < 8:
        suggestions.append("Password is too short! Use at least 8 characters.")
        score -= 2  # Heavy penalty for passwords too short

    # Check password length
    elif len(password) < 10:
        suggestions.append("Make your password at least 10 characters long.")
        score -= 1

    # Check for common words
    has_common, word = contains_common_word(password, common_words)
    if has_common:
        suggestions.append(f"Don't use common words or patterns like '{word}'.")
        score -= 1

    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        suggestions.append("Avoid repeating the same character multiple times.")
        score -= 1

    # Check for consecutive characters
    if is_sequential(password):
        suggestions.append("Avoid sequences like 'abc' or '123'.")
        score -= 1

    # Check for keyboard patterns
    if is_keyboard_pattern(password):
        suggestions.append("Avoid keyboard patterns like 'qwerty' or 'asdf'.")
        score -= 1

    # Check for mixed character types
    categories = {
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digits": any(c.isdigit() for c in password),
        "symbols": any(c in string.punctuation for c in password),
    }
    if sum(categories.values()) < 4:
        suggestions.append("Use a password that contaions a mix of uppercase, lowercase, numbers, and symbols.")
        score -= 2

    #Eveluate the final score
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }[max(score, 0)]

    #Return the results
    return {
        "password": password,
        "strength": strength,
        "score": score,
        "suggestions": suggestions
    }

# Main function to run the password strength checker
# This function loads common passwords, prompts the user for a password, and evaluates its strength.
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    print("Type 'exit' to quit.\n")

    # Load common passwords
    common_words = load_common_words("/Users/adamalazzawi/Desktop/Final Project/10-million-password-list-top-100000.txt")

    # Check if common words were loaded successfully
    if not common_words:
        print("\nPlease make sure the file '10-million-password-list-top-100000' is in the same folder.\n")
    else:
        # Prompt the user for a password and evaluate its strength
        while True:
            user_password = input("Enter a password to evaluate (or type 'exit'): ").strip()
            if user_password.lower() == "exit":
                print("\nGoodbye! 👋")
                break
            
            # Check for short passwords
            if len(user_password) < 6:
                print("\n Password must be at least 6 characters long. Try again.\n")
                continue
            
        
            # This function evaluates the password strength and provides suggestions for improvement.
            result = evaluate_password_strength(user_password, common_words)

            # Print the results and suggestions
            print(f"\nPassword: {result['password']}")
            print(f"Strength: {result['strength']} ({result['score']}/5)")
            if result['suggestions']:
                print("Suggestions:")
                for s in result['suggestions']:
                    print(f" - {s}")
            print("-" * 40)
