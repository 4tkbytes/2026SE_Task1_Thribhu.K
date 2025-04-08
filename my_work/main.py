import sys
import getpass

def quit():
    print("Goodbye, see you later :)")
    sys.exit(0)

def write(username:str, password:str):
    # check if user already exists
    with open("my_work/pass.csv", 'r') as file:
        for line in file:
            if username in line:
                print("User already exists, therefore unable to create new user. Returning back to main menu.")
                return
    
    # append item to file
    with open("my_work/pass.csv", "a") as file:
        file.write(f"{username},{password}")
    return

def login():
    raise NotImplementedError("Login")

def register():
    # check if file exists, if not create a new one
    try:
        file = open("my_work/pass.csv")
        file.close()
    except:
        print("File doesn't exist, initialising new pass file")
        file = open("my_work/pass.csv", "w")
        file.close()
    
    # ask user for their username and password
    username = input("Enter your username: ")
    while True:
        password = getpass.getpass("Enter your password (No password echo for security purposes): ", )
        reconfirm_password = getpass.getpass("Reconfirm your password: ")
        if password == reconfirm_password:
            print("Password confirmed!")
            break
        else:
            continue
    
    # write the content to a file
    write(username, password)
    print("Successfully created new user, returning back to main menu!")

def main():
    while True:
        user_count = 0 # change user count later
        # create main menu
        print(f"""
    ===========================
        Example Auth Client
    ===========================
        Choose your option
        ---
        [1] - Login
        [2] - Register
        
        [q] - Quit
    ===========================
    Stats: {user_count} users on platform
    ===========================
        """)
        choice = input("Choice: ").lower()

        match choice:
            case 'q':
                quit()
                break
            case '1':
                login()
                break
            case '2':
                register()
                break
            case _:
                print("Unable to determine choice, returning back to main menu")
                break
        continue

if __name__ == '__main__':
    main()