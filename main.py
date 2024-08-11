import random
import string


print("*********************Made for PRACTICE*********************")

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+<>?/\\|~:;.,"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, note=None):
    with open("saved_passwords.txt", "a") as file:
        file.write("************************\n")
        file.write(f"Password: {password}\n")
        if note:
            file.write(f"Note: {note}\n")
        file.write("************************\n")
    print("Password saved!")

def main():
    print("Password Generator")
    print("------------------")

    while True:
        try:
            length = int(input("Enter the desired length for your password: "))

            if length <= 0:
                print("Length must be greater than zero.")
                continue

            password = generate_password(length)
            print(f"Your generated password is: {password}")

            while True:
                option = input("Would you like to (T)ry another password or (S)ave this one? ").lower()
                if option == 't':
                    break
                elif option == 's':
                    note = input("Enter a note to save with the password (optional): ")
                    save_password(password, note)
                    return
                else:
                    print("Invalid option. Please enter 'T' to try another or 'S' to save.")

        except ValueError:
            print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
