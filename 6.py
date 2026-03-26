# Custom Exceptions
class UsernameNotUnique(Exception):
    pass

class InvalidAge(Exception):
    pass

class UnderAge(Exception):
    pass

class InvalidEmail(Exception):
    pass


# Step 1: Take all user data and store it
users = []

n = int(input("Enter number of users: "))

for i in range(n):
    username = input("Enter username: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    users.append((username, email, age))   # storing tuple

# Step 2: Directory to store valid users
directory = {}

# Step 3: Iterate and check errors
for username, email, age in users:
    try:

        # username check
        if username in directory:
            raise UsernameNotUnique

        # age validation
        if not age.isdigit():
            raise InvalidAge

        age = int(age)

        if age <= 0:
            raise InvalidAge

        if age < 16:
            raise UnderAge

        # email validation
        if "@" not in email or "." not in email.split("@")[-1]:
            raise InvalidEmail

        # add user (age not stored)
        directory[username] = email
        print(username, "added successfully")

    except UsernameNotUnique:
        print("Error:", username, "username is not unique")

    except InvalidAge:
        print("Error:", username, "age is not a positive integer")

    except UnderAge:
        print("Error:", username, "is under 16")

    except InvalidEmail:
        print("Error:", email, "is not valid")


print("\nFinal Directory:")
print(directory)