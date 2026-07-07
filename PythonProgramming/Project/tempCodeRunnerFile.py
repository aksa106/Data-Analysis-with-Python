def user_management():

    users = ["rahul", "aman", "priya"]

    while True:

        print("\n===== USER MANAGEMENT SYSTEM =====")
        print("1. Register User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "3":
            print("Program Closed.")
            break

        elif choice == "2":

            if not users:
                print("No users found.")
                continue

            print("\nRegistered Users:")

            for user in users:
                print(user)

        elif choice == "1":

            username = input("Enter Username: ").lower()
            age = int(input("Enter Age: "))
            role = input("Enter Role (admin/user): ").lower()
            is_verified = input("Account Verified? (yes/no): ").lower() == "yes"

            if username in users:
                print("Username already exists.")

            elif age < 18:
                print("User must be at least 18 years old.")

            elif role not in ["admin", "user"]:
                print("Invalid role.")

            elif not is_verified:
                print("Please verify your account.")

            else:
                users.append(username)

                print("\nRegistration Successful!")
                print(f"Username : {username}")
                print(f"Role     : {role}")
                print(f"Age      : {age}")

        else:
            print("Invalid Choice.")