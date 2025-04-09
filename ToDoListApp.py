def showMenu():
    print("1. Add Task")
    print("2. View Task")
    print("3.Remove Task")
    print("4. Exit")

def ToDoApp():
    print("Welcome Task Manager Apps")
    print("Developed By Arfin Shariar")
    todo = []
    while True:
        showMenu()
        choice = input("Enter Your Choice: ")

        #Choice == 1
        if choice == "1": #For Task add
            task = input("Enter the task: ")
            todo.append(task)
            print("✅ Task is added")

        elif choice == "2": #If any task exist
            print("\nYour Task:")
            if todo:
                for i,task in enumerate(todo, start=1):
                    print(f"{i}.{task}")

            else:
                print("No Task Found!") #If there is no task in the system

        elif choice == "3": #Remove a Task from the list
            print("\nRemove a Task")
            for i,task in enumerate(todo,start=1):
                print(f"{i}.{task}")
            try:
                task_num = int(input("Enter Task Number: "))
                if 1<=task_num <= len(todo):
                    removed = todo.pop(task_num-1)
                else:
                    print("Invalid Task Number")
            except ValueError:
                print("Please Enter a Valid Number!")

        elif choice == "4":
            print("Exiting TodoList App!")
            print("Bye Bye")
            break

        else:
            print("Invalid Choice! Choose between 1-4")

ToDoApp()
