from csv_1 import load_users_from_csv, save_users_to_csv

users = {}

while True:
    recuperando = load_users_from_csv('users.csv')
    users = recuperando
    print("\nUser Manager:")
    print("1. Add user")
    print("2. Remove user")
    print("3. List all users")
    print("4. Search user by email")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        
        if email in users:
            print("User with this email already exists.")
        else:
            users[email] = name
            print(f"{name} added successfully!")
            save_users_to_csv('users.csv', users)

    elif choice == "2":
        email = input("Enter email to remove: ")
        
        if email in users:
            del users[email]
            print(f"User with email {email} removed successfully!")
            save_users_to_csv('users.csv', users)
        else:
            print("User not found.")

    elif choice == "3":
        if not users:
            print("No users in the list.")
        else:
            for email, name in users.items():
                print(f"Name: {name}, Email: {email}")

    elif choice == "4":
        email = input("Enter email to search: ")
        
        if email in users:
            print(f"Name: {users[email]}, Email: {email}")
        else:
            print("User not found.")

    elif choice == "5":
        print("Goodbye!")
        break
