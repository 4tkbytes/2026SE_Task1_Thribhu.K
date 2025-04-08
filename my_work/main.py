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
                print("User already exists, therefore unable to create new user. Returning")
                return "User already exists"
    
    # append item to file
    with open("my_work/pass.csv", "a") as file:
        file.write(f"{username},{password}\n")
    return ""

def search_file_k(file_path:str, keyword:str):
    # searches file using path and keyword, then returns the key and value
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                return line.strip().split(',')
        print("Keyword does not exist")
        return

def post_auth_menu():
    raise NotImplementedError("You have arrived at the post auth menu hooray!")

def login():
    username = input("Input your username: ")
    password = getpass.getpass("Input your password (No echo): ")
    
    search = search_file_k("my_work/pass.csv", username)
    try:
        if password in search:
            print("Authentication successfull!")
        else:
            print("Password is not correct, returning back to main menu")
            return "Incorrect Password!"
    except Exception:
        print("Username not found in database, returning back to main menu")
        return "Username not found in login"
    post_auth_menu()
    return ""

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
            print("Password not the same, please re-enter it again")
            continue
    
    # write the content to a file
    errString = write(username, password)
    if len(errString) != 0:
        print("Error creating new user")
        return errString
    print("Successfully created new user, returning back to main menu!")
    return ""

def check_user_count():
    try:
        line_count = 0
        with open("my_work/pass.csv") as file:
            for line in file:
                line_count+=1
        return line_count
    except:
        return 0

def main():
    err_string = ""

    while True:
        # create main menu
        user_count = check_user_count()
        print(len(err_string))
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
    {"Error: " if not len(err_string) == 0 else ""}{err_string if not len(err_string) == 0 else "    No errors reported"}
    ===========================
        """)
        choice = input("Choice: ").lower()

        match choice:
            case 'q':
                quit()
                break
            case '1':
                err_string = login()
            case '2':
                err_string = register()
            case _:
                print("Unable to determine choice, returning back to main menu")
                err_string = "Choose correctly >:("
        continue

if __name__ == '__main__':
    main()