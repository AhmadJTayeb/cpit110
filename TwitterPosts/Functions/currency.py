# Format the result message
def formatString(currency, fromAmount, toAmount):
    return f"{fromAmount:.2f} {currency} = {toAmount:.2f} SAR"

# Convert Dollar to SAR
def fromDollar(x):
    result = x * 3.75
    print(formatString("$", x, result))

# Convert Euro to SAR
def fromEuro(x):
    result = x * 4.14
    print(formatString("€", x, result))

# Check if the selected value is in the menu
def check(currency):
    return not (1 <= currency <= 2)

# Display the menu and get the user choice
def getUserChoice():
    print("Select the currency: ")
    print("(1) Dollar")
    print("(2) Euro")
    currency = eval(input("Enter your choice: "))
    return currency

# Get the correct currency of the entered amount from the user
def getCurrency():
    while True:
        currency = getUserChoice()

        if check(currency):
            print("Wrong Choice ! ... Try again.\n")
        else:
            break
    return currency

# Print the entered amount in SAR
def printInSaudiRiyalCurrency(currency, amount):
    if amount <= 0:
        return False

    if currency == 1:
        fromDollar(amount)
    else:
        fromEuro(amount)

    print("--------------------")
    return True

# Get the amount from the user
def getAmount():
    return eval(input("Enter the amount: "))

# Main function
def main():
    again = True
    while again:
        again = printInSaudiRiyalCurrency(getCurrency(), getAmount())
    print("\nGoodbye :)")

if __name__ == '__main__':
    main()