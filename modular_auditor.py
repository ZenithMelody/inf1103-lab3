inventory = 0
failed_Enteries = 0

while True:

    user_Input = input("Enter stock (or quit to exit): ")

    if user_Input == "quit":
            break

    # reject digits and negatives
    if not user_Input.isdigit():
         print("Try again")
         failed_Enteries += 1
         continue

    amount = int(user_Input)


    inventory += amount

    # state management
    print(f"Added {amount} | Current Inventory: {inventory}")

    if inventory > 500:
        print("Over limit of 500")
        break

print("\nReport Summary")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_Enteries}")