import tkinter as tk


def get_values():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    return num1, num2


def inset_values(value):
    ans_entry.delete(0, 'end')
    ans_entry.insert(0, value)


def plus():
    num1, num2 = get_values()
    res = num1 + num2
    inset_values(res)


def minus():
    num1, num2 = get_values()
    res = num1 - num2
    inset_values(res)


def multi():
    num1, num2 = get_values()
    res = num1 * num2
    inset_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    inset_values(res)

win = tk.Tk()

win.title('Калькулятор')
win.geometry("400x500")
win.resizable(False, False)
but_plus = tk.Button(win, text="+", width=2, height=2, command=plus)
but_plus.place(x=100, y=200)
but_minus = tk.Button(win, text="-", width=2, height=2, command=minus)
but_minus.place(x=150, y=200)
but_multi = tk.Button(win, text="*", width=2, height=2, command=multi)
but_multi.place(x=200, y=200)
but_div = tk.Button(win, text="/", width=2, height=2, command=div)
but_div.place(x=250, y=200)

num1_entry = tk.Entry(win, width=30)
num1_entry.place(x=100, y=75)
num2_entry = tk.Entry(win, width=30)
num2_entry.place(x=100, y=150)
ans_entry = tk.Entry(win, width=30)
ans_entry.place(x=100, y=300)

num1_label = tk.Label(win, text="Введите первое число:")
num1_label.place(x=100, y=50)
num2_label = tk.Label(win, text="Введите второе число:")
num2_label.place(x=100, y=125)
ans_label = tk.Label(win, text="Ответ:")
ans_label.place(x=100, y=275)



win.mainloop()