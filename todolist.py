class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"[{'x' if self.completed else ' '}] {self.title}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

if __name__ == "__main__":
    todo = TodoList()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. List Tasks\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Task title: ")
            todo.add_task(title)
        elif choice == '2':
            todo.list_tasks()
            idx = int(input("Task number to complete: ")) - 1
            todo.complete_task(idx)
        elif choice == '3':
            todo.list_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
