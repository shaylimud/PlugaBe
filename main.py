import tkinter as tk
from tkinter import ttk, messagebox

from pluga_beit_hr.dataset import load_people, append_person


def add_person() -> None:
    first = first_var.get().strip()
    last = last_var.get().strip()
    phone = phone_var.get().strip()
    if not first or not last or not phone:
        messagebox.showwarning("Missing data", "Please fill all fields")
        return
    append_person({"first_name": first, "last_name": last, "phone_number": phone})
    first_var.set("")
    last_var.set("")
    phone_var.set("")
    refresh_data()


def refresh_data() -> None:
    listbox.delete(0, tk.END)
    for row in load_people():
        display = f"{row['first_name']} {row['last_name']} - {row['phone_number']}"
        listbox.insert(tk.END, display)


root = tk.Tk()
root.title("People Manager")

first_var = tk.StringVar()
last_var = tk.StringVar()
phone_var = tk.StringVar()

# Form fields
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(1, weight=1)

ttk.Label(frame, text="First name").grid(row=0, column=0, sticky=tk.W)
first_entry = ttk.Entry(frame, textvariable=first_var)
first_entry.grid(row=0, column=1, sticky="ew")

ttk.Label(frame, text="Last name").grid(row=1, column=0, sticky=tk.W)
last_entry = ttk.Entry(frame, textvariable=last_var)
last_entry.grid(row=1, column=1, sticky="ew")

ttk.Label(frame, text="Phone").grid(row=2, column=0, sticky=tk.W)
phone_entry = ttk.Entry(frame, textvariable=phone_var)
phone_entry.grid(row=2, column=1, sticky="ew")

button_frame = ttk.Frame(frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=5)

add_button = ttk.Button(button_frame, text="Add", command=add_person)
add_button.pack(side=tk.LEFT, padx=5)

show_button = ttk.Button(button_frame, text="Show data", command=refresh_data)
show_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

refresh_data()

root.mainloop()
