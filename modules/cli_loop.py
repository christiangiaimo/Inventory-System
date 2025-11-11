
from inventory_validator import *
from data_converter import *
from prompts import *
from cash_flow import *
from main import cash_flow

def cli_loop(completer, style,bottom_toolbar):
    while True:
        html_completer = FuzzyWordCompleter(options)
        text =  prompt(
            "Enter Product Name: ",
            completer= completer,
            complete_while_typing=True,
            #validator = validator_instance,
            style = style,
            show_frame = True,
            bottom_toolbar = bottom_toolbar
        )

        text_parts = text.split()


        # This is the search part, it asks for search
        #In this fisrt part it functions with the show all option
        match text_parts:    
            case ['search',_,'show_all']: 
                    product_name = text_parts[1]
                    product_data = inv_data.searh_products(product_name)

                    print ("\n" + "="*50)
                    print(f"searched product: {text}")
                    print("=" * 50)
                    print(product_data.to_string(index= False))

            case ['search',_,"cost"]:
                    product_name = text_parts[1]
                    product_data = inv_data.searh_products(product_name)
                    cost = product_data['cost'].iloc[0]
                    print("\n" + "="*50)  
                    print(f"searched product: {text}")
                    print ("="*50)       
                    print(f"product cost: {cost}")

            case['search',_,"quantity"]:
                    product_name = text_parts[1]
                    product_data = inv_data.searh_products(product_name)
                    quantity = product_data['quantity'].iloc[0]
                    print("\n" + "="*50)  
                    print(f"searched product: {text}")
                    print ("="*50)       
                    print(f"product quantity: {quantity}")


            case['search',_,'Purchase']:
                product_name = text_parts[1]
                product_data = inv_data.searh_products(product_name)
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

            case['search',_,'purchase']:
                product_name = text_parts[1]
                product_data = inv_data.searh_products(product_name)

                quantity = product_data['quantity'].iloc[0]
                new_qty = int(dialog_window())
                cost = int(add_new_dialog_cost_window())
                inv_data.increment_quantity(product_name,new_qty)
                cash_flow.add_expense(cost)
                print("\n" + "="*50)  
                print(f"Changed product: {text}")
                print ("="*50)       
                print(f"changed stock product to: {quantity}")    



            case['search',_,'sell']:
                product_name = text_parts[1]
                product_data = inv_data.searh_products(product_name)
                quantity = product_data['quantity'].iloc[0]
                cost = int(add_new_dialog_sell_window())

                inv_data.product_sell(product_name,dialog)
                cash_flow.add_income(cost)
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



            case['show_cash_flow']:
                df = cash_flow.cash_flow
                print ("\n" + "="*50)
                print(f"searched product: {text}")
                print("=" * 50)
                print(df.to_string(index= False))

            case['exit']:
                inv_data.export_json()
                cash_flow.export_cash_flow_json()
                break           
                            

            #case['add_new']:
            #      if len(text_parts) > 1:
            #         inv_data.insert_product(text_parts[1])