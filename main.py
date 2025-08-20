from task_manager import *

def main():
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter task description: ")
            add_task(task)
        elif choice == '3':
            task_id = int(input("Enter task number to mark completed: "))
            mark_task_done(task_id)
        elif choice == '4':
            task_id = int(input("Enter task number to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()