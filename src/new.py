from datetime import datetime

# Initialize as an empty list, not [dict]
tasks = []

def add_task(task, priority):
    task_object = {
        "task": task,
        "is_completed": False,
        "time": datetime.now(),
        "priority": priority
    }
    tasks.append(task_object)

def list_task():
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} | Priority: {task['priority']} | Completed: {task['is_completed']} | Time: {task['time'].strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    while True:
        user_task = input("Enter the task (or type 'done' to finish): ")
        if user_task.lower() == "done":
            break
        task_priority = input("Enter the priority level: ")
        add_task(user_task, task_priority)

    list_task()

