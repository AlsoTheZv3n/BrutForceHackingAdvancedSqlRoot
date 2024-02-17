import subprocess
import os

# Function to get new passwords from user input
def get_new_passwords():
    new_passwords = []
    print("Enter new passwords (type 'done' when finished):")
    while True:
        new_password = input("> ")
        if new_password.lower() == 'done':
            break
        new_passwords.append(new_password)
    return new_passwords

# Function to get new MySQL bin directory path from user input
def get_new_mysql_bin_dir():
    return input("Enter the new MySQL bin directory path: ")

# Define the MySQL bin directory path (raw)
mysql_bin_dir = r"C:\Program Files\MySQL\MySQL Server 8.0\bin"

# Get new MySQL bin directory path from user input
new_mysql_bin_dir = get_new_mysql_bin_dir()

# Check if the new path is provided, if not, keep the default path
if new_mysql_bin_dir:
    mysql_bin_dir = new_mysql_bin_dir

# Array of passwords to try
passwords = [
    "password1",
    "password2",
    "password3",
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "123456789",
    "12345678910",
    "hallo",
    "hallo26",
    "password",
    "randompassword",
    "securepassword",
    "mysql123",
    "admin123",
    "qwerty",
    "letmein",
    "password123",
    "1234567890",
    "password!",
    "welcome",
    "monkey",
    "abc123",
    "123qwe",
    "passw0rd",
    "master",
    "football",
    "dragon",
    "123123",
]

# Get new passwords from user input
new_passwords = get_new_passwords()
if new_passwords:
    passwords.extend(new_passwords)

# Boolean flag to track success
login_successful = False

# Loop through each password
for password in passwords:
    # Construct the command to execute
    executable = os.path.join(mysql_bin_dir, "mysql.exe")
    arguments = f"-u root -p{password}"

    # Execute the command
    process = subprocess.Popen([executable] + arguments.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, _ = process.communicate()

    # Check if MySQL login was successful
    if process.returncode == 0:
        print("Login successful!")
        login_successful = True
        break  # Exit the loop if login is successful
    else:
        print("Login unsuccessful. Trying next password...")

# If none of the passwords worked
if not login_successful:
    print("Unable to login to MySQL with any of the provided passwords.")
