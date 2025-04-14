def display_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in your list.")

def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, index):
    if 0 < index <= len(tasks):
        tasks.pop(index - 1)
    else:
        print("Invalid task index.")

# Main logic
tasks = []
while True:
    print("\nTo-Do List Menu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        display_tasks(tasks)
    elif choice == '2':
        task = input("Enter task to add: ")
        add_task(tasks, task)
    elif choice == '3':
        display_tasks(tasks)
        try:
            task_index = int(input("Enter task number to remove: "))
            remove_task(tasks, task_index)
        except ValueError:
            print("Invalid input! Please enter a valid task number.")
    elif choice == '4':
        break
    else:
        print("Invalid choice! Please try again.")
