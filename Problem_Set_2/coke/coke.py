def main():

    print("Amount Due: 50")
    amount_due = int(50)
    total_inserted = int(0)
    calculate_payment(amount_due, total_inserted)

def calculate_payment(amount_due, total_inserted):
    while amount_due > 0:
        coin = int(input ("Insert Coin: "))

        if coin in [5, 10, 25]:
            amount_due -= coin
            total_inserted += coin
        else:
            print(f"Amount Due: {amount_due}")

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

    if total_inserted > 50:
        change =int(0)
        change = total_inserted - 50
        print(f"\n Change Owed: {change}")
    elif total_inserted == 50:
        print("Change Owed: 0")

main()