import tkinter

from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfile(initialfile="/", title="Выберете файл",
                                      filetypes=(("Текстовый документ", ".txt"),
                                                 ("Все файлы", "*")))
    text['text'] = text['text'] + ' ' + filename.name

window = tkinter.Tk()
window.title("Проводник")
window.geometry('400x100')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=2, width=40, background='gray')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, height=2, width=12, text="Выбрать файл", command=file_select)
button_select.grid(column=2, row=1)
window.mainloop()