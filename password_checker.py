import re

# Password list
passwords = ["Hello@123", "weak", "Strong1!", "nospecia1"]

# Function to check password strength
def validate_password(pwd):
    has_length = len(pwd) >= 8
    has_number = any(c.isdigit() for c in pwd)
    has_special = bool(re.search(r'[!@#$%^&*]', pwd))

    return has_length and has_number and has_special

# Store results
results = {}

for pwd in passwords:
    if validate_password(pwd):
        results[pwd] = "Valid"
    else:
        results[pwd] = "Invalid"

# Display results
print("Password Check Results:")
for pwd, status in results.items():
    print(f"{pwd}: {status}")

# Search feature
search = input("\nSearch password: ")

if search in results:
    print(f"{search}: {results[search]}")
else:
    print("Password not found.")

# Save to file
with open("password_results.txt", "w") as f:
    for pwd, status in results.items():
        f.write(f"{pwd}: {status}\n")

print("\nResults saved to password_results.txt")