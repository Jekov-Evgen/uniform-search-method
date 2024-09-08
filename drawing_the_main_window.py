from tkinter import *
from tkinter import ttk
from results_window import ResultWindow

class MainWindow:
    def window(self):
        root = Tk()
        root.title("Равномерный перебор")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        
        data_rendering = ResultWindow()
        
        ttk.Label(frm, text='Добро пожаловать!').grid(column=0, row=0)
        ttk.Label(frm, 
                  text='Эта программа выдаст результат равномерного перебора функции').grid(column=0, row=1)
        ttk.Label(frm, 
                  text='Для получения значений нажмите внизу на кнопку с текстом функций').grid(column=0, row=2)
        ttk.Button(frm, text='e^x+1/x', command=data_rendering.result_window).grid(column=0, row=3)
        
        root.mainloop()