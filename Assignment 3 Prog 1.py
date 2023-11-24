def main():
    # Prices of apples and oranges
    apple_price = 20
    orange_price = 25

    # Asking user for the quantities of apples and oranges
    print("\tWelcome to the PUP Fruit Shop!")
    print("-------------------------------------------")
    apples = int(input("Number of apples you want to buy: "))
    oranges = int(input("Number of oranges you want to buy: "))
    print("-------------------------------------------")

    # Calculating total costs
    total_cost = (apples * apple_price) + (oranges * orange_price)

    # Displaying the total amount to be paid in a stylized format
    print("\tThank you for shopping with us!")
    print("-------------------------------------------")
    print("ITEM\t\tQUANTITY\tPRICE")
    print("-------------------------------------------")
    print(f"Apples\t\t{apples}\t\t{apples * apple_price} pesos")
    print(f"Oranges\t\t{oranges}\t\t{oranges * orange_price} pesos")
    print("-------------------------------------------")
    print(f"TOTAL AMOUNT:\t\t\t{total_cost} pesos")
    print("-------------------------------------------")

if __name__ == "__main__":
    main()