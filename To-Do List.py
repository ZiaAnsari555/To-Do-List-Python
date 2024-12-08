tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    action = input("Enter 'add' to add a task or 'show' to view tasks: ").lower()
    if action == 'add':
        task = input("Enter task: ")
        add_task(task)
    elif action == 'show':
        show_tasks()
    else:
        print("Invalid input.")
