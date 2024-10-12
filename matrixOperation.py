import copy 
class matrixOperation():
    def __init__(self, rows:int,columns:int, matrix):
        self.matrix = matrix
        self.columns = columns
        self.rows = rows
    
    def are_all_value_of_row_is_zero(self,row:int):
        for i in range(0,self.columns):
            if self.matrix[row][i] != 0 :
                return False
        return True
            
    def leading_coefficient(self,row:int):
        for i in range(0,self.columns):
            if self.matrix[row][i]==1:
                return i
            elif self.matrix[row][i]==0:
                pass
            else :
                return -1
        return -1
    
    def check_ref(self):
        if (self.rows == 1) :
            if (self.are_all_value_of_row_is_zero(0) or self.leading_coefficient(0) != -1) :
                return True
            else :
                return False
        
        for i in range(1,self.rows):
            if ((self.leading_coefficient(i-1) != -1 or self.are_all_value_of_row_is_zero(i-1)) 
                and (self.leading_coefficient(i) != -1 or self.are_all_value_of_row_is_zero(i))) :
                if (self.leading_coefficient(i-1) != -1 and self.leading_coefficient(i) !=-1):
                    if (self.leading_coefficient(i-1) < self.leading_coefficient(i)):
                        pass
                    else :
                        return False
                elif (self.leading_coefficient(i-1) != -1 and self.are_all_value_of_row_is_zero(i)):
                    pass
                elif (self.are_all_value_of_row_is_zero(i-1) and self.are_all_value_of_row_is_zero(i)):
                    pass
                else:
                    return False
            else:
                return False
        return True

    def check_rref(self):
        if (self.check_ref()) :
            for i in range(0,self.rows):
                if self.leading_coefficient(i) != -1:
                    for j in range(0,self.rows):
                        if self.matrix[j][self.leading_coefficient(i-1)]==0:
                            pass
                        elif i==j:
                            pass
                        else:
                            return False
            return True
        return False
            
    def multiplying_row_by_constant(self,row:int,constant:float):
        if(constant == 0):
            return
        else:
            for i in range(0,self.columns):
                if (self.matrix[row][i] == 0) :
                    pass
                else:
                    self.matrix[row][i] = self.matrix[row][i] * constant

    def adding_row_by_row(self,row_1:int,row_2:int,constant:float):
        if(constant == 0):
            return
        else:
            for i in range(0,self.columns):
                self.matrix[row_1][i] = self.matrix[row_1][i]  + (self.matrix[row_2][i]*constant)

    def switching_two_rows(self,row_1:int,row_2:int):
        for i in range(0,self.columns):
            tmp = self.matrix[row_1][i]
            self.matrix[row_1][i] = self.matrix[row_2][i]
            self.matrix[row_2][i] = tmp

    def calulate_rref(self):
        answer = {
            "matrix": [],
            "operation": []
        }
        leading_coefficient_position_in_row = 0
        for i in range(0, self.columns):
            j = 0
            while j < self.rows:
                if leading_coefficient_position_in_row != -1:
                    if self.matrix[leading_coefficient_position_in_row][i] == 1:
                        if leading_coefficient_position_in_row != j and self.matrix[j][i] != 0:
                            answer["operation"].append(f'R{j+1} = R{j+1}+({-1*self.matrix[j][i]})R{leading_coefficient_position_in_row+1}')
                            self.adding_row_by_row(j, leading_coefficient_position_in_row, -1*self.matrix[j][i])
                            answer["matrix"].append(copy.deepcopy(self.matrix))  
                    elif self.matrix[j][i] != 0 and leading_coefficient_position_in_row <= j:
                        if j != leading_coefficient_position_in_row:
                            answer["operation"].append(f'R{j+1}<->R{leading_coefficient_position_in_row+1}')
                            self.switching_two_rows(j, leading_coefficient_position_in_row)
                            answer["matrix"].append(copy.deepcopy(self.matrix))  
                        if self.matrix[leading_coefficient_position_in_row][i] != 1:
                            answer["operation"].append(f'R{leading_coefficient_position_in_row+1} = R{leading_coefficient_position_in_row+1}/{self.matrix[leading_coefficient_position_in_row][i]}')
                            self.multiplying_row_by_constant(leading_coefficient_position_in_row, 1/self.matrix[leading_coefficient_position_in_row][i])
                            answer["matrix"].append(copy.deepcopy(self.matrix)) 
                        j = -1
                j += 1

            if leading_coefficient_position_in_row == -1:
                pass
            elif self.matrix[leading_coefficient_position_in_row][i] == 1:
                leading_coefficient_position_in_row += 1
                if leading_coefficient_position_in_row == self.rows:
                    leading_coefficient_position_in_row = -1
                
        return answer

    def calculate_ref(self):
        answer = {
            "matrix": [],
            "operation": []
        }
        leading_coefficient_position_in_row = 0
        for i in range(0, self.columns):
            j = 0
            while j < self.rows:
                if leading_coefficient_position_in_row != -1:
                    if self.matrix[leading_coefficient_position_in_row][i] == 1:  
                        if (leading_coefficient_position_in_row != j and self.matrix[j][i] != 0 and leading_coefficient_position_in_row < j):
                            answer["operation"].append(f'R{j+1} = R{j+1}+({-1*self.matrix[j][i]})R{leading_coefficient_position_in_row+1}')
                            self.adding_row_by_row(j, leading_coefficient_position_in_row, -1*self.matrix[j][i])
                            answer["matrix"].append(copy.deepcopy(self.matrix))
                    elif (self.matrix[j][i] != 0 and leading_coefficient_position_in_row <= j):
                        if j != leading_coefficient_position_in_row:
                            answer["operation"].append(f'R{j+1}<->R{leading_coefficient_position_in_row+1}')
                            self.switching_two_rows(j, leading_coefficient_position_in_row)
                            answer["matrix"].append(copy.deepcopy(self.matrix))  
                        if self.matrix[leading_coefficient_position_in_row][i] != 1:
                            answer["operation"].append(f'R{leading_coefficient_position_in_row+1} = R{leading_coefficient_position_in_row+1}/{self.matrix[leading_coefficient_position_in_row][i]}')
                            self.multiplying_row_by_constant(leading_coefficient_position_in_row, 1/self.matrix[leading_coefficient_position_in_row][i])
                            answer["matrix"].append(copy.deepcopy(self.matrix)) 
                        j = -1
                j += 1
            if leading_coefficient_position_in_row == -1:
                pass
            elif self.matrix[leading_coefficient_position_in_row][i] == 1:
                leading_coefficient_position_in_row += 1
                if leading_coefficient_position_in_row == self.rows:
                    leading_coefficient_position_in_row = -1
        return answer
