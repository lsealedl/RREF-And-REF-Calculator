import dearpygui.dearpygui as dpg
class createTable():
    def __init__(self, row:int,column:int,parent, max_row:int, max_column:int):
        self.rowSize = row
        self.columnSize = column
        self.parent = parent 
        for i in range(0,max_row):
            if i == 0:
                self.table =[[]]
                self.group = [0] 
            else:   
                self.table.append([])
                self.group.append(0)
  
            for j in range(0,max_column):
                self.table[i].append(0)

        for i in range(0,row):
            with dpg.group(parent=self.parent , horizontal=True) as self.group[i]:
                pass
            for j in range(0,column):
                self.table[i][j]=dpg.add_input_float(parent=self.group[i], step=0,width=80)
    def getData(self):
        print(dpg.get_value(self.table[0][0]))
    def setMatirxSize(self,row:int,column:int):
        if row>self.rowSize:
            tmp_row = row
        else:
            tmp_row=self.rowSize

        if column>self.columnSize:
            tmp_column = column
        else:
            tmp_column=self.columnSize

        for i in range(0 ,tmp_row):
            if(i>=self.rowSize):
                with dpg.group(parent=self.parent , horizontal=True) as self.group[i]:
                    pass
            for j in range(0,tmp_column):
                if(i>=self.rowSize or j>=self.columnSize):
                    self.table[i][j]=dpg.add_input_float(parent=self.group[i], step=0,width=80)
                if(i>=row or j>=column):
                    dpg.delete_item(self.table[i][j])
            if(i>=row):
                dpg.delete_item(self.group[i])
        self.rowSize=row
        self.columnSize=column
    
    def getMatrixData(self):
        result = []
        for i in range(0,self.rowSize):
            result.append([])
            for j in range(0,self.columnSize):
                result[i].append(dpg.get_value(self.table[i][j]))       
        return result
    

       