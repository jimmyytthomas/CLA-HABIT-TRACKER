#GOAL = should let a user track daily habit from the terminal, save progress between runs, and view simple stats. This is a good next step because it adds persistent data, multiple features that interact, and strong dictionary/file handling practice.
import datetime
import json




last_reset_date = datetime.date.today()

#todays todo uploaded from the todo list in the json


# Load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as f: #open file in read mode 
            content = f.read().strip() # read everything from the file and remove extra spaces
            if not content: # if the file is empty, return an empty list
                return [] 
            return json.loads(content) # convert JSON string into a Python list/dictionary
    except: # if file doesn't exist or JSON is broken, return empty list
        return []
       





def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)
tasks = load_tasks()
#tasks.append({"name": "Homework", "done": False, "created_at": last_reset_date})
#save_tasks(tasks)
todays_tasks = tasks

# Add a task

        

#Main menu
while True:
    habit_number = 0
    for task in tasks:
        habit_number += 1
        print("habit #",habit_number,task['name'])
    print("Type 1,2,3 based on the options below: ")
    mainmenu = int(input("1. Add habit \n2. Mark Complete \n3. Delete Habit \n4. Quit \nYou choose: "))
    if mainmenu not in [1,2,3,4]:
        print("Invalid option try again")
        continue
    if mainmenu == 1:
        add_to_list = input("What daily habit would you like to add? or type ""back to menu"" to return to menu: ").lower()
        if add_to_list == "back to menu":
            continue
        else:
            tasks.append({"name": add_to_list, "done": False, "created_at": str(last_reset_date)})
            save_tasks(tasks)
            print(tasks)
            
    elif mainmenu == 2:
        break #mark a habit complete for the day
    elif mainmenu == 3:
        delete_from_list = input("What daily habit would you like to delete, select based on number. or type ""back to menu"" to return to menu: ").lower()
        if delete_from_list == "back to menu":
            continue
        else:
            delete_from_list = int(delete_from_list)
            tasks.remove(tasks[delete_from_list-1])
            save_tasks(tasks)
            
    elif mainmenu == 4:
        break #quit program
    
        

