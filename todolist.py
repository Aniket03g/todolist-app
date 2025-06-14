import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, title, completed=False, bookmarked=False):
        self.title = title
        self.completed = completed
        self.bookmarked = bookmarked

    def __repr__(self):
        bookmark = '★' if self.bookmarked else ' '
        return f"[{'x' if self.completed else ' '}] {bookmark} {self.title}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def bookmark_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].bookmarked = not self.tasks[index].bookmarked

    def list_tasks(self, only_bookmarked=False):
        if only_bookmarked:
            return [task for task in self.tasks if task.bookmarked]
        return self.tasks

# --- Tkinter UI ---
class TodoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.title("To-Do List App")
        self.geometry("400x400")
        self.todo_list = todo_list
        self.show_only_bookmarked = tk.BooleanVar()
        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self, width=50)
        self.task_listbox.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Complete Task", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Bookmark", command=self.bookmark_task).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(self, text="Show only bookmarked", variable=self.show_only_bookmarked, command=self.refresh_tasks).pack(pady=5)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.todo_list.list_tasks(only_bookmarked=self.show_only_bookmarked.get())
        for i, task in enumerate(tasks):
            self.task_listbox.insert(tk.END, f"{i+1}. {task}")

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Task title:")
        if title:
            self.todo_list.add_task(title)
            self.refresh_tasks()

    def complete_task(self):
        idx = self.task_listbox.curselection()
        tasks = self.todo_list.list_tasks(only_bookmarked=self.show_only_bookmarked.get())
        if idx:
            # Map index in filtered list to index in full list
            task = tasks[idx[0]]
            full_idx = self.todo_list.tasks.index(task)
            self.todo_list.complete_task(full_idx)
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Select a task to complete.")

    def bookmark_task(self):
        idx = self.task_listbox.curselection()
        tasks = self.todo_list.list_tasks(only_bookmarked=self.show_only_bookmarked.get())
        if idx:
            task = tasks[idx[0]]
            full_idx = self.todo_list.tasks.index(task)
            self.todo_list.bookmark_task(full_idx)
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Select a task to bookmark.")

if __name__ == "__main__":
    todo = TodoList()
    app = TodoApp(todo)
    app.mainloop()
