from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.validation import Validator, ValidationError
import asyncio
from inventory import *
from product import *


inv_data = inventory()
options = inv_data.inventory['name'].tolist()
#Shows the list of the names in the inventory

PROPERTIES = {
    'cost': None,
    'quantity': None,
    'show_all':  None,
    'purchase': None,
    'sell': None
}


nested_options = {} 


for name in options:
    nested_options[name] = PROPERTIES

final_completer_dict = {
    'search':nested_options,
    'show_cash_flow':None,
    'add_new': None,
    'exit': None,
    
}    

class InventoryValidator(Validator):
    def __init__(self, valid_names):
        self.valid_names = valid_names


    def validate(self, document):
        text = document.text.strip()
        if text not in options:
            raise ValidationError(
                message = f"{text} is not a valid name. Please select one of the tags in the options displayed",
                cursor_position = len(document.text)
            )

    async def validate_async(self, document):
        # Await ensures it runs without blocking the event loop
        await asyncio.to_thread(self.validate, document) 
