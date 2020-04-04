while True:
    while True:
        print("Select the currency: ")
        print("(1) Dollar")
        print("(2) Euro")
        currency = eval(input("Enter your choice: "))

        if not (1 <= currency <= 2):
            print("Wrong Choice ! ... Try again.\n")
        else:
            break
    amount = eval(input("Enter the amount: "))
    if amount <= 0:
        break

    if currency == 1:
        print(f"{amount:.2f} $ = {amount * 3.75:.2f} SAR")
    else:
        print(f"{amount:.2f} € = {amount * 4.14:.2f} SAR")

print("\nGoodbye :)")