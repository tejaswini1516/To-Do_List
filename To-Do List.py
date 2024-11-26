import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def delete_all_tasks():
    if messagebox.askyesno("Confirmation", "Do you want to delete all tasks?"):
        tasks_listbox.delete(0, tk.END)

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("To-Do List Manager - JAVATPOINT")
root.geometry("500x400")
root.configure(bg="beige")


title_label = tk.Label(root, text="The To-Do List", font=("Brush Script MT", 24, "italic"), bg="beige", fg="brown")
title_label.pack(pady=10)

main_frame = tk.Frame(root, bg="beige")
main_frame.pack(pady=10)

task_frame = tk.Frame(main_frame, bg="beige")
task_frame.grid(row=0, column=0, padx=10)

task_label = tk.Label(task_frame, text="Enter the Task:", font=("Arial", 12, "bold"), bg="beige", fg="black")
task_label.pack(pady=5)

task_entry = tk.Entry(task_frame, width=25, font=("Arial", 12))
task_entry.pack(pady=5)

add_task_button = tk.Button(task_frame, text="Add Task", font=("Arial", 10, "bold"), command=add_task, bg="white", fg="black", width=15)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(task_frame, text="Delete Task", font=("Arial", 10, "bold"), command=delete_task, bg="white", fg="black", width=15)
delete_task_button.pack(pady=5)

delete_all_button = tk.Button(task_frame, text="Delete All Tasks", font=("Arial", 10, "bold"), command=delete_all_tasks, bg="white", fg="black", width=15)
delete_all_button.pack(pady=5)

exit_button = tk.Button(task_frame, text="Exit", font=("Arial", 10, "bold"), command=exit_app, bg="white", fg="black", width=15)
exit_button.pack(pady=5)

tasks_listbox = tk.Listbox(main_frame, font=("Arial", 12), height=15, width=25, bg="white", fg="black")
tasks_listbox.grid(row=0, column=1, padx=10)

root.mainloop()
