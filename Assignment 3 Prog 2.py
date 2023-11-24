def calculate_max_apples(money, price_per_apple):
    maximum_apples = money // price_per_apple  # Calculate the maximum number of apples
    remaining_money = money % price_per_apple  # Calculate the remaining money

    return maximum_apples, remaining_money

def main():
    try:
        money = float(input("Amount of money you have: Php "))
        price_per_apple = float(input("Price of an apple: Php "))

        if money < 0 or price_per_apple <= 0:
            print("Please enter valid amounts (greater than zero).")
        else:
            maximum_apples, remaining_money = calculate_max_apples(money, price_per_apple)
            print(f"With Php {money:.2f}, you can buy {maximum_apples} apple(s) and have Php {remaining_money:.2f} remaining.")
    
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()