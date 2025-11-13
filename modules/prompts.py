from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.styles import Style

example_style = Style.from_dict({
    # --- Fondos  ---
    'dialog': 'bg:#D3D3D3',
    'dialog.body': 'bg:#F5F5F5',
    'dialog shadow': 'bg:#A9A9A9',
    
    # --- Texto (Se mantiene oscuro) ---
    'dialog.body label': '#4F4F4F',
    'frame.label': '#708090 bold',
    
    # --- Botones y Foco ---
    'button': 'bg:#EBEBEB #4F4F4F',
    
  #--- Fondo Azul Brillante, Texto Blanco, Negrita.
    'button.focused': 'bg:#007ACC fg:#FFFFFF bold', 
    

})



def dialog_window():
    text = input_dialog(
        title = 'Amount',
        text = 'Please type the amount to change:',
        style = example_style).run()
    if text == "" or text is None:
        raise Exception("Not a valid input")
    return text



def add_new_dialog_fam_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the family name of the product:',
        style = example_style).run() 
    if text == "" or text is None:
        raise Exception("Not a valid input")

        
    return text

def add_new_dialog_name_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the name of the product:',
       style = example_style).run()
    if text == "" or text is None:
        raise Exception("Not a valid input")    

    return text

def add_new_dialog_cost_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the cost of the product:',
        style = example_style).run()
    if text == "" or text is None:
        raise Exception("Not a valid input")
    
    return text

def add_new_dialog_unit_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the measurement unit of the product:',
        style = example_style).run()
    if text == "" or text is None:
        raise Exception("Not a valid input")
    return text

def add_new_dialog_quantity_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the initial quantity of the product:',
        style = example_style).run()
    if text == "" or text is None:
         raise Exception("Not a valid input")
    
    return text

def add_new_dialog_sell_window():
    text = input_dialog(
        title = 'Sell product',
        text = 'Please type the quantity of the product you are selling:',
        style = example_style).run()
    if text == "" or text is None:
        raise Exception("Not a valid input")
    
    return text
