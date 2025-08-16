"""to_do_list = [
    {
        "task": "Take a shower",
        "priority": "High",
        "completed": True,
        "duration_minutes": 15,
        "tags": ["hygiene", "morning", "self-care"]
    },
"""

def main_menu():
    print("""
------------ The To-Do List Program ----------------

Enter the appropriate number to choose an option:

1 - Create a list
2 - View your list(s)
3 - Update your list(s)
4 - Delete your list(s)
5 - Exit program

----------------------------------------------------    
    """)

main_menu()

while True:

    try:
        chosen_option = int(input("Your Option: "))
    except ValueError:
        print("Please choose a valid option from 1 - 5.")
        continue

    if chosen_option == 1:
        print("You chose option 1")
    elif chosen_option == 2:
        print("You chose option 2")
    elif chosen_option == 3:
        print("You chose option 3")
    elif chosen_option == 4:
        print("You chose option 4")
    elif chosen_option == 5:
        print("Exiting program...")
        break
    else:
        print("Please choose a valid option from 1 - 5.")
