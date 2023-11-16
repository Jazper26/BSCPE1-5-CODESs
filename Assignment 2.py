# The function of these is to display seperate lines
def display_separator():
    print("=" * 40)

# Inputting User Information
def get_user_info():
    while True:
        name = input("Enter your name: ")
        while True:
            age = input("Enter your age: ")
            if age.isdigit() and int(age) >= 0:
                break
            else:
                print("Please enter a valid age.")
        address = input("Enter your address: ")
        return name, age, address

# Displaying user information
def display_user_info(name, age, address):
    display_separator()
    print("\tUser Information")
    display_separator()
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")

    display_separator()

# Get user information
user_name, user_age, user_address = get_user_info()

# Display user information
display_user_info(user_name, user_age, user_address)
