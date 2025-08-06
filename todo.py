import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n" + "="*40)
    print("      TO-DO LIST APPLICATION")
    print("="*40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("0. Exit")
    print("="*40)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Empty task cannot be added.")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(tasks):
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirm == 'y':
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Clear cancelled.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (0-4): ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            clear_tasks(tasks)
        elif choice == '0':
            print("Exiting To-Do App. Have a productive day!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
