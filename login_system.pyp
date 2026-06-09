import datetime

try:
    credentials = {}

    with open("credentials.txt", "r") as f:
        for line in f:
            user, pwd = line.strip().split(":")
            credentials[user] = pwd

    print("Credentials loaded.")

    username = input("Username: ")
    password = input("Password: ")

    success = credentials.get(username) == password

    if success:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    status = "SUCCESS" if success else "FAILED"

    with open("login_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | {username} | {status}\n")

    print(f"Login {status.lower()}. Attempt logged.")

except FileNotFoundError:
    print("Error: credentials.txt not found!")

except ValueError:
    print("Error: Malformed credentials file.")
