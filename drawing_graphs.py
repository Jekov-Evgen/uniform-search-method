from execution_of_program_logic import UniformSearch, DataGeneration
import matplotlib.pyplot as plt

class Graphics:
    def __init__(self) -> None:
        _data_cerate = UniformSearch()
        _data_control = DataGeneration()
        _data_cerate.uniform_search_logic()
        _data_cerate.function_for_plotting()
        
        self._data_X = _data_control.getting_X()
        self._data_FX = _data_control.getting_FX()
        self._data_FXmin = _data_control.getting_FXmin()
        self._data_Xmin = _data_control.getting_Xmin()
        
    def graph_of_a_function(self):
        fig = plt.figure(num='График функции')
        plt.plot(self._data_X, self._data_FX, marker='o', markersize=5, label='e^x + 1/x')
        plt.title("График функции")
        plt.legend()
        plt.grid(True)
        plt.show()