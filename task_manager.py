import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{idx + 1}. {task['task']} [{status}]")

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def mark_task_done(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed.")
    else:
        print("❌ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑 Deleted task: {removed['task']}")
    else:
        print("❌ Invalid task number.")