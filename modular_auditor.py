inventory = 0
failed_Enteries = 0

# handles prompt, input validation / return valid ints or 'quit' signal
def get_valid_input():
        global failed_Enteries # it could not access it without the global
        while True:
                user_Input = input("Enter stock or quit to exit: ")
                if user_Input.lower() == "quit":
                        return "quit"
                
                if not user_Input.isdigit():
                        print("Try again")
                        failed_Enteries += 1
                        continue
                
                return int(user_Input)

def generate_report(inventory, failed_Enteries):
        print("\nReport Summary")
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {failed_Enteries}")
        
while True:

    user_Input = get_valid_input()

    if user_Input == "quit":
            break

    amount = int(user_Input)


    inventory += amount

    # state management
    print(f"Added {amount} | Current Inventory: {inventory}")

    if inventory > 500:
        print("Over limit of 500")
        break

generate_report(inventory, failed_Enteries)