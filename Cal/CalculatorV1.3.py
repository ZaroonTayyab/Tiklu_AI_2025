import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Zaroon's CAL V1.3")
root.geometry("400x600")
root.configure(bg="#121212")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 28), bg="#1e1e1e", fg="white", borderwidth=0, relief="flat", justify="right")
entry.pack(fill="both", padx=20, pady=(20,10), ipady=15)


def click(symbol):
    entry.insert(tk.END, str(symbol))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Syntax ERROR..")


def create_button(frame, text, command, color="#272727", fg="white"):
    btn = tk.Button(frame, text=text, font=("Arial", 20), bg=color, fg=fg, bd=0, relief="flat",
                    command=command, activebackground="#333333", activeforeground="white")
    btn.pack(side="left", expand=True, fill="both", padx=5, pady=5, ipadx=10, ipady=10)
    return btn


button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["(", "C", "⌫","="]
]

for row in button_rows:
    frame = tk.Frame(root, bg="#121212")
    frame.pack(expand=True, fill="both", padx=10)
    for btn_text in row:
        if btn_text == "=":
            create_button(frame, btn_text, calculate, color="#00C853")
        elif btn_text == "C":
            create_button(frame, btn_text, clear, color="#D50000")
        elif btn_text == "⌫":
            create_button(frame, btn_text, backspace, color="#FF6F00")
        else:
            create_button(frame, btn_text, lambda symbol=btn_text: click(symbol))


for child in root.winfo_children():
    if isinstance(child, tk.Frame):
        for button in child.winfo_children():
            button.configure(highlightthickness=0, bd=0, relief="flat")

root.mainloop()
