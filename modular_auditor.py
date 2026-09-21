inventory = 0
failed_Enteries = 0
total_Tax = 0.0

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

# finds new total
def process_delivery(current_total, new_value):
        return current_total + new_value

def calculate_tax(amount):
        return amount * 0.10

# report summary generation
def generate_report(inventory, failed_Enteries, total_Tax):
        print("\nReport Summary")
        print(f"Total Units Processed: {inventory}")
        print(f"Total amount of Tax: {total_Tax:.2f}")
        print(f"Number of Failed/Rejected Entries: {failed_Enteries}")
        
while True:

    user_Input = get_valid_input()

    if user_Input == "quit":
            break

    tax = calculate_tax(user_Input)
    total_Tax += tax
    inventory = process_delivery(inventory, user_Input)

    # state management
    print(f"Added {user_Input} | Tax: {tax:.2f} | Current Inventory: {inventory}")

    if inventory > 500:
        print("Over limit of 500")
        break

generate_report(inventory, failed_Enteries, total_Tax)