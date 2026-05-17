# ==========================================
#        TO-DO LIST APPLICATION
# ==========================================
# Features:
# ✔ Add Tasks
# ✔ View Tasks
# ✔ Update Tasks
# ✔ Delete Tasks
# ✔ Mark Tasks as Completed
# ✔ Save Tasks in File
# ✔ Load Tasks Automatically
# ==========================================

import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

# ------------------------------
# Load tasks from file
# ------------------------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# ------------------------------
# Save tasks to file
# ------------------------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ------------------------------
# Display Menu
# ------------------------------
def show_menu():
    print("\n========== TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("=====================================")

# ------------------------------
# Add Task
# ------------------------------
def add_task():
    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks()

    print("✅ Task added successfully!")

# ------------------------------
# View Tasks
# ------------------------------
def view_tasks():
    if not tasks:
        print("📂 No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "❌ Pending"

        print(f"{index}. {task['task']} --> {status}")

# ------------------------------
# Update Task
# ------------------------------
def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to update: "))

        if 1 <= task_number <= len(tasks):

            new_task = input("Enter new task name: ")

            tasks[task_number - 1]["task"] = new_task

            save_tasks()

            print("✅ Task updated successfully!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ------------------------------
# Delete Task
# ------------------------------
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            removed_task = tasks.pop(task_number - 1)

            save_tasks()

            print(f"🗑 Task '{removed_task['task']}' deleted successfully!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ------------------------------
# Mark Task as Completed
# ------------------------------
def mark_completed():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            save_tasks()

            print("✅ Task marked as completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ------------------------------
# Main Program
# ------------------------------
tasks = load_tasks()

while True:

    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        print("\n👋 Exiting To-Do List Application...")
        print("Thank you for using the app!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
