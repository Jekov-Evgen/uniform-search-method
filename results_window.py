from execution_of_program_logic import UniformSearch, DataGeneration
from tkinter import *
from tkinter import ttk
from drawing_graphs import Graphics

class ResultWindow:
    def __init__(self) -> None:
        _data_cerate = UniformSearch()
        _data_control = DataGeneration()
        _data_cerate.uniform_search_logic()
        _data_cerate.function_for_plotting()
        
        self._data_X = _data_control.getting_X()
        self._data_FX = _data_control.getting_FX()
        self._data_FXmin = _data_control.getting_FXmin()
        self._data_Xmin = _data_control.getting_Xmin()
        
    def result_window(self):
        root = Tk()
        root.title("Результаты равномерного перебора")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        
        graph_output = Graphics()
        
        ttk.Label(frm, text='X', padding=10).grid(column=0, row=0)
        ttk.Label(frm, text='F(x)', padding=10).grid(column=1, row=0)
        ttk.Label(frm, text='Xmin', padding=10).grid(column=2, row=0)
        ttk.Label(frm, text='F(Xmin)', padding=10).grid(column=3, row=0)
        
        for i in range(len(self._data_X)):
            ttk.Label(frm, text=f'{self._data_X[i]}', padding=10).grid(column=0, row=i + 1)
            ttk.Label(frm, text=f'{self._data_FX[i]}', padding=10).grid(column=1, row=i + 1)
            ttk.Label(frm, text=f'{self._data_Xmin[i]}', padding=10).grid(column=2, row=i + 1)
            ttk.Label(frm, text=f'{self._data_FXmin[i]}', padding=10).grid(column=3, row=i + 1)
        
        ttk.Button(frm, text='Получить график функции', padding=10, command=graph_output.graph_of_a_function).grid(column=1, row=13)
            
        root.mainloop()