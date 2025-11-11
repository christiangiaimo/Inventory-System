from prompt_toolkit.shortcuts import input_dialog


def dialog_window():
    text = input_dialog(
        title = 'Amount',
        text = 'Please type the amount to change:').run()
    return text



def add_new_dialog_fam_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the family name of the product:').run()
    return text

def add_new_dialog_name_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the name of the product:').run()
    return text

def add_new_dialog_cost_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the cost of the product:').run()
    return text

def add_new_dialog_unit_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the measurement unit of the product:').run()
    return text

def add_new_dialog_quantity_window():
    text = input_dialog(
        title = 'New product',
        text = 'Please type the initial quantity of the product:').run()
    return text