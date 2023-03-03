import tkinter as tk
import tkinter.messagebox
import random as rd
import string

LETTERS = [letter for letter in string.ascii_letters]
DIGITS = [num for num in range(10)]
SYMBOLS = [sym for sym in string.punctuation if
           sym != "'" and sym != "\\" and sym != '/' and sym != '//' and sym != "//" and sym != '"']


def generate_pwd():
    letters_list = []
    num_list = []
    sym_list = []
    letter_count = letters_entry.get()
    num_count = num_entry.get()
    sym_count = symbols_entry.get()
    try:
        letter_count = int(letter_count)

    except:
        letter_count = 0
    finally:
        for i in range(letter_count):
            letters_list.append(rd.choice(LETTERS))
    try:
        num_count = int(num_count)
    except:
        num_count = 0
    finally:
        for i in range(num_count):
            num_list.append(rd.choice(DIGITS))

    try:
        sym_count = int(sym_count)
    except:
        sym_count = 0
    finally:
        for i in range(sym_count):
            sym_list.append(rd.choice(SYMBOLS))

    num_list = [str(x) for x in num_list]
    if len(letters_list) <= 30 and len(num_list) <=30 and len(sym_list) <=30:
        pwd_list = letters_list + num_list + sym_list
        rd.shuffle(pwd_list)
        pwd = ''.join(pwd_list)
        pwd_entry.delete(0, tk.END)
        window.clipboard_clear()
        pwd_entry.insert(0, pwd)
        window.clipboard_append(pwd)
    else:
        tk.messagebox.showerror(message="Za duzo znakow")


"""Setting up window"""
window = tk.Tk()
window.config(padx=30, pady=30)
window.title("Password Generator")
"""Digits"""
num_label = tk.Label(text="ile cyfr", pady=10)
num_label.grid(column=0, row=0)
num_entry = tk.Entry()
num_entry.grid(column=1, row=0)

"""Leters"""
letters_label = tk.Label(text="ile liter", pady=10)
letters_label.grid(column=0, row=1)
letters_entry = tk.Entry()
letters_entry.grid(column=1, row=1)

"""Symbols"""
symbols_label = tk.Label(text="ile symboli", pady=5)
symbols_label.grid(column=0, row=2)
symbols_entry = tk.Entry()
symbols_entry.grid(column=1, row=2)

"""Generated Password"""
password_btn = tk.Button(text="Generate password", pady=5, command=generate_pwd)
password_btn.grid(columnspan=2, row= 3)
pwd_label = tk.Label(text="Twoje hasło: ")
pwd_label.grid(column=0, row=4)
pwd_entry = tk.Entry(width=30)

pwd_entry.grid(column=1, row=4)

window.mainloop()