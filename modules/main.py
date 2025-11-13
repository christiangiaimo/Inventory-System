from inventory import *
from product import *
from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.completion import FuzzyWordCompleter, NestedCompleter
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from inventory_validator import *
from data_converter import *
from prompts import *
from cli_loop import *
from cash_flow import *




inv_data = inventory()
cash_flow = Cash_Flow()
options = inv_data.inventory['name'].tolist()




validator = FuzzyWordCompleter(options)
# This takes the options from inventory_validator module 
validator_instance = InventoryValidator(options)
data = {
    'Search': final_completer_dict,
    'New': None,
    'New transaction': None,
    'Delete': None,
    'Exit':None
}
completer = NestedCompleter.from_nested_dict(final_completer_dict)


style = Style.from_dict(
    {
        "frame.border": "#884444",
    }
)
# this is the style for the frame


def bottom_toolbar():
    return(HTML(f" Press <b>[Up]</b>/<b>[Down]</b> to select, <b>[Enter]</b> to accept. Options are: {f"{list(final_completer_dict.keys())[0:3]},etc"}, exit"))

                        


       

if __name__ == '__main__':
    main_loop(completer,style,bottom_toolbar())

                     
    # this prints the data of the dataframe
    #elif:
     #   print("Error: Product not found after validation")    





#print(f"You said: {text}")



#print("Initiating inventory system")
#print("Welcome")