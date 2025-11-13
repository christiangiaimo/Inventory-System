
from inventory_validator import *
from data_converter import *
from prompts import *
from cash_flow import *
from main import cash_flow,completer,style,bottom_toolbar
from prompt_toolkit.styles import Style

#style_from_dict = Style.from_dict(
 #   {
  #      # Default style.
   #     "": "#ff0066",
    #   # Prompt.
     #   "username": "#884444 italic",
      #  "at": "#00aa00",
       # "colon": "#00aa00",
        #"pound": "#00aa00",
       
       # "host": "#000088 bg:#aaaaff",
        #"path": "#884444 underline",
        #"pygments.comment": "#888888 bold",
        #"ygments.keyword": "#ff88ff bold",
        # Make a selection reverse/underlined.
        # (Use Control-Space to select.)
       # "selected-text": "reverse underline",
    #}
#)


#This ask the first question to the user
def first_input():
    first_input = choice(
    message = "Please choose an option",
    options = [("Search","Search Product"),
                ("New","New"),
                ("Show_cash_flow", "Show Cash Flow"),
                ("Exit", "Exit")],
    default = "Search",
)
    return first_input




def cli_loop(completer, style,bottom_toolbar):
    while True:
        html_completer = FuzzyWordCompleter(options)
        text =  prompt(
            "Enter Product Name: ",
            completer= completer,
            complete_while_typing=True,
            #validator = validator_instance,
            style = style,
            # example style style = style_from_dict,
            show_frame = True,
            bottom_toolbar = bottom_toolbar
        )

        text_parts = text.split()
        product_name = text_parts[0]
        product_data = inv_data.searh_products(product_name) 


        # This is the search part, it asks for search
        #In this fisrt part it functions with the show all option
        match text_parts:    
            
            case [_,'show_all']: 
                    print ("\n" + "="*50)
                    print(f"searched product: {text}")
                    print("=" * 50)
                    print(product_data.to_string(index= False))

            case [_,"cost"]:
                    
                    cost = product_data['cost'].iloc[0]
                    print("\n" + "="*50)  
                    print(f"searched product: {text}")
                    print ("="*50)       
                    print(f"product cost: {cost}")

            case[_,"quantity"]:
                    quantity = product_data['quantity'].iloc[0]
                    print("\n" + "="*50)  
                    print(f"searched product: {text}")
                    print ("="*50)       
                    print(f"product quantity: {quantity}")


            case[_,'Purchase']:
                #quantity_prompt = prompt("Update quantity: ")
                #added_quantity = quantity_prompt
                quantity = product_data['quantity'].iloc[0]
                dialog = int(dialog_window())
                cost = int(add_new_dialog_cost_window())
                inv_data.update_quantity(product_name,dialog)
                cash_flow.add_expense(cost)
               # cash_flow.add_expense()
                print("\n" + "="*50)  
                print(f"Changed product: {text}")
                print ("="*50)       
                print(f"changed stock product to: {quantity}")

            case[_,'purchase']:
                quantity = product_data['quantity'].iloc[0]
                new_qty = int(dialog_window())
                cost = int(add_new_dialog_cost_window())
                inv_data.increment_quantity(product_name,new_qty)
                cash_flow.add_expense(cost * new_qty)
                print("\n" + "="*50)  
                print(f"Changed product: {text}")
                print ("="*50)       
                print(f"changed stock product to: {quantity}")    



            case[_,'sell']:
                quantity = product_data['quantity'].iloc[0]
                sell_qty = int(add_new_dialog_sell_window())
                cost = int(add_new_dialog_cost_window())
                inv_data.product_sell(product_name,sell_qty,cost)
                cash_flow.add_income(cost * sell_qty)
                print("\n" + "="*50)  
                print(f"Changed product: {text}")
                print ("="*50)       
                print(f"changed stock product to: {quantity}") 



            case['add_new']:
                family = (add_new_dialog_fam_window())
                name = (add_new_dialog_name_window())
                msr = (add_new_dialog_unit_window())
                cost = int(add_new_dialog_cost_window())
                qty = int(add_new_dialog_quantity_window())
                inv_data.insert_product(family,name,cost,msr,qty)
                inv_data.export_json()
                inv_data.load_json()
                print("\n" + "="*50)  
                print(f"Created new product: {name}")

            case['exit']:
                inv_data.export_json()
                cash_flow.export_cash_flow_json()
                second_input(completer,style,bottom_toolbar)
                 


def show_cash_flow():
    df = cash_flow.cash_flow
    print ("\n" + "="*50)
    print("Showing Cash Flow:")
    print("=" * 50)
    print(df.to_string(index= False))

def exit() :
    inv_data.export_json()
    cash_flow.export_cash_flow_json()
    exit                 
                            

            #case['add_new']:
            #      if len(text_parts) > 1:
            #         inv_data.insert_product(text_parts[1])



def second_input(completer,style,bottom_toolbar):
     first_ipt = first_input()
     match first_ipt:
          case "Search":
               cli_loop(completer,style,bottom_toolbar)
          case  "Show_cash_flow":
               show_cash_flow()
          case "New":
                family = (add_new_dialog_fam_window())
                name = (add_new_dialog_name_window())
                msr = (add_new_dialog_unit_window())
                cost = int(add_new_dialog_cost_window())
                qty = int(add_new_dialog_quantity_window())
                inv_data.insert_product(family,name,cost,msr,qty)
                inv_data.export_json()
                inv_data.load_json()
                print("\n" + "="*50)  
                print(f"Created new product: {name}")
          case "exit":
               exit

                    
                     




