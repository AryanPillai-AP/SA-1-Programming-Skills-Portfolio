#Exercise 6: Brute Force Attack

def check_password():
    CORRECT_PASSWORD = "12345"
    MAX_ATTEMPTS = 5
    attempts = 0
    
    print("Welcome to the Security System")
    print("Please enter the password.")
    print(f"You have {MAX_ATTEMPTS} attempts remaining.\n")
    
    while attempts < MAX_ATTEMPTS:
        password = input("Enter password: ")
        attempts += 1
        
        if password == CORRECT_PASSWORD:
            print("\nAccess Granted! Welcome to the system.")
            return True
        else:
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"\nIncorrect password!")
                print(f"You have {remaining} {'attempt' if remaining == 1 else 'attempts'} remaining.")
                print("Please try again.\n")
            else:
                print("\nSECURITY ALERT!")
                print("Maximum attempts reached!")
                print("The authorities have been notified.")
                print("System locked.")
                return False

if __name__ == "__main__":
    check_password()