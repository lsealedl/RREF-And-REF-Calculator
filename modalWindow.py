import dearpygui.dearpygui as dpg

class createStepWindow():
    def __init__(self, rows:int,columns:int, tag:str, matrix):
        with dpg.window( modal=True, show=True, tag=tag, no_title_bar=True):
            with dpg.table(header_row=False,borders_innerH=True):
                dpg.add_table_column()
                for i in range(0,len(matrix['matrix'])):
                    with dpg.table_row():
                        with dpg.group():
                            for k in range(0,rows):
                                with dpg.group(horizontal=True):
                                    for j in range(0,columns):
                                        with dpg.group():
                                            dpg.add_text(f'{matrix['matrix'][i][k][j]} ',)
                    with dpg.table_row():
                        dpg.add_text(f'{matrix['operation'][i]}')
            dpg.add_separator()
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item(tag, show=False))

class createCheckedResultWindow():
    def __init__(self,text:str, tag:str):
        with dpg.window(modal=True, show=True, tag=tag, no_title_bar=True , min_size=[100,50]):
            dpg.add_text(f'{text}')
            dpg.add_separator()
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item(tag, show=False))
