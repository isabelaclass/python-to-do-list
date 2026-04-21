tasks = []

print("Welcome to the Task Manager!")

while True:
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    option = int(input("Please choose an option: "))

    match option:
        case 1:
            task = input("Enter the task: ")
            task_id = len(tasks) + 1
            tasks.append(f"{task_id} - {task}")
            print("Task added successfully!")
        case 2:
            if not tasks:
                print("No tasks found.")
            else:
                print("Your tasks:")
                for task in tasks:
                    print(task)
        case 3:
            task_to_delete = int(input("Enter the task id: "))
            tasks.pop(task_to_delete - 1)
            print("Task deleted successfully!")
        case 4:
            break
        case _:
            print("Invalid option, please try again.")