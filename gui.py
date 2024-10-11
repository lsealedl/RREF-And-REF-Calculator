import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from createTable import createTable
from resultWindow import createResultWindow
from matrixOperation import matrixOperation
MAX_MATRIX_ROW = 20
MAX_MATRIX_COLUMN = 20
def save_callback():
    print("Save Clicked")

def setMatirxSizebyEnter():
    table.setMatirxSize(dpg.get_value(row_size),dpg.get_value(column_size))

def showValue():
    a = table.getMatrixData()
    print(a)

def showCalculateRREFResult():
    dpg.delete_item('modal_id')
    matrixOp = matrixOperation(dpg.get_value(row_size),dpg.get_value(column_size),table.getMatrixData())
    createResultWindow(dpg.get_value(row_size),dpg.get_value(column_size),"modal_id",matrixOp.calulate_rref())

dpg.create_context()
dpg.create_viewport( width=600, height=200)
dpg.setup_dearpygui()

demo.show_demo()

with dpg.window(label="Example Window" ) as mainWindow:
    with dpg.group(horizontal=True):
        row_size = dpg.add_input_int(width=100 ,default_value=3,
                          min_clamped=True ,min_value=1,
                          max_clamped=True ,max_value=MAX_MATRIX_ROW,
                          label="Row Size",
                          callback=setMatirxSizebyEnter) 
        dpg.add_button(label="Enter Matrix Size",callback=setMatirxSizebyEnter)
        column_size = dpg.add_input_int(width=100 ,default_value=3,
                          min_clamped=True ,min_value=1,
                          max_clamped=True ,max_value=MAX_MATRIX_COLUMN,
                          label="Column Size",
                          callback=setMatirxSizebyEnter) 
    with dpg.group() as mid:
        pass

    dpg.add_button(label="Reset Matrix")
    with dpg.group(horizontal=True):
        with dpg.group():
            dpg.add_button(label="Check REF")
            dpg.add_button(label="Calculate REF")
        with dpg.group():
            dpg.add_button(label="Check RREF")
            dpg.add_button(label="Calculate RREF",callback=showCalculateRREFResult)
    dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))
    dpg.add_button(label="show value",callback=showValue)

        
    table = createTable(3,3,mid,max_row=20,max_column=20)

    dpg.add_text("Hello world")

    dpg.add_text("Hello world")
    # dpg.add_button(label="Save")
    # dpg.add_input_text(label="string")
    # dpg.add_slider_float(label="float")

# dpg.set_primary_window(mainWindow, True)


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


