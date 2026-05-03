from db import session, Task, logger
from sqlalchemy.exc import SQLAlchemyError  

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
            desc = input("Enter the task description: ")
            if desc:
                try:
                    new_task = Task(description=desc)
                    session.add(new_task)
                    session.commit()
                    logger.info(f"Added task: {desc}")
                    print("Task added successfully!")
                except SQLAlchemyError as e:
                    session.rollback()
                    logger.error(f"Error adding task: {e}")
                    print(f"Error adding task: {e}")

            else:
                logger.warning("Attempted to add an empty task.")
                print("Task description cannot be empty.")
        case 2:
            tasks = session.query(Task).all()
            if not tasks:
                logger.info("No tasks found when viewing tasks.")
                print("No tasks found.")
            else:
                logger.info(f"Viewing {len(tasks)} tasks.")
                print("Your tasks:")
                for task in tasks:
                    print(f"{task.id}. {task.description}")
        case 3:
            try: 
                task_to_delete = int(input("Enter the task id: "))
                task_to_delete = session.query(Task).filter_by(id=task_to_delete).first()
                if task_to_delete:
                    session.delete(task_to_delete)
                    session.commit()
                    logger.info(f"Deleted task with id: {task_to_delete.id}")
                    print("Task deleted successfully!")
                else:
                    logger.warning("Attempted to delete a non-existent task.")  
                    print("Task not found.")
            except ValueError:
                logger.warning("Invalid input for task id.")
                print("Invalid input. Please enter a valid task id.")
            except SQLAlchemyError as e:
                session.rollback()
                logger.error(f"Error occurred while deleting task: {e}")
        case 4:
            break
        case _:
            logger.warning("Invalid option selected.")
            print("Invalid option, please try again.")