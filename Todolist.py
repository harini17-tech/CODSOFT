import tkinter as tk
from tkinter import messagebox, simpledialog
class ToDoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("To-Do-List")
        self.tasks=[]
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial",12))
        self.task_listbox.pack(pady=10)
        self.entry=tk.Entry(root, width=50, font=("Arial",12))
        self.entry.pack(pady=5)

        tk.Button(root, text="Add Task", command=self.add_task, width=15).pack(pady=2)
        tk.Button(root, text="Update Task", command=self.update_task, width=15).pack(pady=2)
        tk.Button(root, text="Track Task", command=self.track_task, width=15).pack(pady=2)
        tk.Button(root, text="Delete Task", command=self.delete_task, width=15).pack(pady=2)
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task":task,"done":False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error","Task cannot be empty.")
    def update_task(self):
        selected=self.task_listbox.curselection()
        if selected:
            index=selected[0]
            new_task=simpledialog.askstring("Update Task","Enter new task:")
            if new_task:
                self.tasks[index]["task"] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Select Task", "Please select a task to update.")

    def track_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Select Task", "Please select a task to mark as done.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Select Task", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Yes,Done!" if task["done"] else "Not done"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()