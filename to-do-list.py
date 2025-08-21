import json

def content_seperator():
    print("\n")
    print("-------------------------------------")

def create_list():
    
    content_seperator()
    
    list = []

    while True:
        
        outer_flag = False
        entry = {}
        
        entry["task"] = input("Enter a task: ")
        entry["priority"] = input("Enter a priority (Choose between Low, Medium, and High): ")
        entry["completed"] = False #This defaults to 'False' because it is assumed the task has not been completed yet.
        
        while True:
            try:
                entry["duration_minutes"] = int(input("Enter the time this should take to complete in minutes (e.g. 60): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number to represent the time this task will take in minutes.")
                continue

        entry["tags"] = input("Enter a comma-separated list of tags that describe your task. E.g. 'hygiene, morning, self-care': ").split(",")

        list.append(entry)

        while True:
            
            answer = input("Add another entry? Y/N: ")
            if answer == "Y" or answer == "y":
                content_seperator()
                break
            elif answer == "N" or answer == "n":
                outer_flag = True
                break
            else:
                print("Invalid input. Choose between Y or N!")
                continue

        if outer_flag == True:
            break

    with open("lists.json", "a") as file:
        json.dump(list, file)
        file.write("\n")

def read_list():
    
    content_seperator()

    all_tasks = []

    with open("lists.json", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                all_tasks.append(json.loads(line))

    for i, element in enumerate(all_tasks, start=1):
        print(f"=== To-Do List {i} ===")
        for j, task in enumerate(element, start=1):
            print(f"--- Task {j} ---")
            for key, value in task.items():
                if isinstance(value, list):
                    new_list = [string.strip() for string in value]
                    print(", ".join(new_list))
                else:
                    print(f"{key} - {value}")
            print("\n")

def update_list():
    pass

def delete_list():
    pass

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

while True:

    main_menu()
    
    while True:

        try:
            chosen_option = int(input("Your Option: "))
        except ValueError:
            print("Please choose a valid option from 1 - 5.")
            continue
        break

    if chosen_option == 1:
        create_list()
    elif chosen_option == 2:
        read_list()
    elif chosen_option == 3:
        update_list()
    elif chosen_option == 4:
        delete_list()
    elif chosen_option == 5:
        print("Exiting program...")
        break
    else:
        print("Please choose a valid option from 1 - 5.")
