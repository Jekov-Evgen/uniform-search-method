from math import e

class UniformSearch:     
    def _function_calculation(self, _X_value):
        self._X_value = _X_value
        return (e ** self._X_value) + (1 / self._X_value)
    
    def uniform_search_logic(self):
        left_border = 0.5
        right_border = 1
        permissible_error = 0.05
        self.segments = [i for i in range(0, 11)]
        all_iterations = []
        
        number_of_segments = (right_border - left_border) / permissible_error
        step_size = (right_border - left_border) / number_of_segments
        
        minimum = self._function_calculation(left_border)
        X_minimum = left_border
        
        for i in range(0, int(number_of_segments + 1)):
            self.segments[i] = left_border + i * step_size
            
            if self._function_calculation(self.segments[i]) < minimum:
                minimum = self._function_calculation(self.segments[i])
                X_minimum = self.segments[i]
            temp = [round(minimum, 3), round(X_minimum, 3)]
            all_iterations.append(temp)
            
        final_result = round(self._function_calculation(X_minimum), 4)
        
        return (all_iterations, final_result)
    
    def function_for_plotting(self):
        data = self.segments
        function_execution_result = []
        
        for i in range(len(data)):
            data[i] = round(data[i], 2)
            function_execution_result.append(self._function_calculation(data[i]))
            function_execution_result[i] = round(function_execution_result[i], 3)
        
        return (data, function_execution_result)

class DataGeneration:
    def getting_FX(self):
        class_call = UniformSearch()
        class_call.uniform_search_logic()
        temp = class_call.function_for_plotting()
        data = temp[1]
        
        return data
    
    def getting_X(self):
        class_call = UniformSearch()
        class_call.uniform_search_logic()
        temp = class_call.function_for_plotting()
        data = temp[0]
        
        return data
    
    def getting_Xmin(self):
        class_call = UniformSearch()
        temp = class_call.uniform_search_logic()
        data = []
        
        for i in range(len(temp[0])):
            data.append(temp[0][i])
            data[i] = data[i][1]
            
        return data
    
    def getting_FXmin(self):
        class_call = UniformSearch()
        temp = class_call.uniform_search_logic()
        data = []
        
        for i in range(len(temp[0])):
            data.append(temp[0][i])
            data[i] = data[i][0]
            
        return data        