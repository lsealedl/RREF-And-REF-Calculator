import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from createTable import createTable
from modalWindow import createStepWindow, createCheckedResultWindow
from matrixOperation import matrixOperation
MAX_MATRIX_ROW = 15
MAX_MATRIX_COLUMN = 15

def setMatirxSizebyEnter():
    table.setMatirxSize(dpg.get_value(row_size),dpg.get_value(column_size))

def resetMatrx():
    table.resetMatrixData()

def showCalculateRREFResult():
    dpg.delete_item('modal')
    matrixOp = matrixOperation(dpg.get_value(row_size),dpg.get_value(column_size),table.getMatrixData())
    if(matrixOp.check_rref()):
        createCheckedResultWindow('It\' already is RREF','modal')
    else:
        createStepWindow(dpg.get_value(row_size),dpg.get_value(column_size),"modal",matrixOp.calulate_rref())

def showCalculateREFResult():
    dpg.delete_item('modal')
    matrixOp = matrixOperation(dpg.get_value(row_size),dpg.get_value(column_size),table.getMatrixData())
    if(matrixOp.check_ref()):
        createCheckedResultWindow('It\' already is REF','modal')
    else:
        createStepWindow(dpg.get_value(row_size),dpg.get_value(column_size),"modal",matrixOp.calculate_ref())


dpg.create_context()
dpg.create_viewport(title="RREF And REF Calculator",width=600, height=200)
dpg.setup_dearpygui()

with dpg.window(label="RREF And REF Calculator" ) as mainWindow:
    with dpg.group(horizontal=True):
        row_size = dpg.add_input_int(width=100 ,default_value=3,
                          min_clamped=True, min_value=1,
                          max_clamped=True, max_value=MAX_MATRIX_ROW,
                          label="Row Size",
                          callback=setMatirxSizebyEnter) 
        dpg.add_button(label="Enter Matrix Size",callback=setMatirxSizebyEnter)
        column_size = dpg.add_input_int(width=100 ,default_value=3,
                          min_clamped=True, min_value=1,
                          max_clamped=True, max_value=MAX_MATRIX_COLUMN,
                          label="Column Size",
                          callback=setMatirxSizebyEnter) 
    with dpg.group() as mid:
        pass

    dpg.add_button(label="Reset Matrix", callback=resetMatrx)
    with dpg.group(horizontal=True):
        with dpg.group():
            dpg.add_button(label="Calculate REF", callback=showCalculateREFResult)
        with dpg.group():
            dpg.add_button(label="Calculate RREF", callback=showCalculateRREFResult)
    
    table = createTable(3, 3, mid,max_row=20, max_column=20)

dpg.set_primary_window(mainWindow, True)

dpg.set_viewport_small_icon('_internal\icon.ico')
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


