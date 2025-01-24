import random
import string

adjectives = ["Happy", "Cool", "Quick", "Bright", "Charming", "Brave", "Funky", "Silent", "Kind", "Gentle"]
nouns = ["Dragon", "Tiger", "Phoenix", "Wizard", "Ranger", "Knight", "Hawk", "Eagle", "Wolf", "Lion"]

def generate_username(include_numbers=True, include_special_chars=True, username_length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice("!@#$%^&*")
    
    if username_length and username_length > len(username):
        extra_chars = random.choices(string.ascii_letters, k=(username_length - len(username)))
        username += ''.join(extra_chars)
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers in usernames? (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters in usernames? (yes/no): ").lower() == "yes"
    username_length = input("Specify username length (or press Enter to skip): ")
    
    username_length = int(username_length) if username_length else None
    
    usernames = []
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars, username_length)
        usernames.append(username)
        print("Generated Username:", username)
    
    save_to_file = input("Would you like to save the usernames to a file? (yes/no): ").lower() == "yes"
    if save_to_file:
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()
