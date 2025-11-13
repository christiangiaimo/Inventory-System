from product import *
import pandas as pd
import os

path = "/home/cgiaimo/Desktop/workspace/github.com/christiangiaimo/Inventory-System/data"
name_file='inventory_data.json'
full_path = os.path.join(path,name_file)


class inventory:
    def __init__(self,filepath = full_path ):
        self.full_path = filepath
        self.inventory = self.load_json()
               
        #self.inventory = pd.DataFrame({'family':['Alimentos','Mamalo'],
         #                             'name':['Cebolla','Chupalo_Andres'],
          #                            'cost':[10,'Tu culo'],
           #                           'unit':['Kg','Ano'],
            #                          'quantity':[10,5]})


    def load_json(self):
        if os.path.exists(self.full_path):
            df = pd.read_json(self.full_path,orient='records')
            return df
        else:
            print("Inventory not found, creating a new Dataframe")
            df = pd.DataFrame({'family':[],
                               'name':[],
                               'cost':[],
                               'unit':[],
                               'quantity':[]})
            return df
        

    def export_json(self):
        self.inventory.to_json(self.full_path, orient ="records", indent=4)    


    def insert_product(self,family,name,cost,unit,quantity):
        new_item = pd.DataFrame({'family':[family],
                                 'name':[name],
                                 'cost':[cost],
                                 'unit':[unit],
                                 'quantity':[quantity]})
        self.inventory = pd.concat(self.inventory,new_item,ignore_index=True)
        print(f"Product {name} added succesfully")

    def searh_products(self, product):
        filtered_product = self.inventory.loc[self.inventory['name'] == product]
        return filtered_product
        
        
    
    def delete_product(self, product):
        mask_to_delete = (self.inventory['name'] == product)
        # 2. Verificar si el item existe antes de eliminarlo
        if mask_to_delete.any():
            # 3. FILTRAR: Sobreescribir el DataFrame con solo las filas que NO coinciden (~) con la mascara.
            self.inventory = self.inventory[~mask_to_delete].reset_index(drop=True)
            print(f"{product}, succesfully deleated.")
        else:
            print(f"Error: Item '{product}' Not found.")
          
        raise Exception("Couldnt complete the deleation")
    
    def insert_product(self,family,name,cost,unit,quantity):
        new_item = pd.DataFrame({'family':[family],
                             'name':[name],
                             'cost':[cost],
                             'unit':[unit],
                             'quantity':[quantity]})
        self.inventory = pd.concat([self.inventory,new_item],ignore_index=True)
        print(f"Product {name} added succesfully")


    def increment_quantity(self, name, amount):
        target_index = self.inventory.index[self.inventory['name'] == name]

        if target_index.empty:
            print(f"Error: Item {name} not found") 
            return
        idx = target_index[0]
        current_quantity = self.inventory.loc[idx, 'quantity']
        new_quantity = current_quantity + amount

        if new_quantity < 0:
            print("{name} new quantity is less than 0 operation cancelled")
            return

        self.inventory.loc[idx,'quantity'] = new_quantity
        print(f"Succesfully change {name} quantity to {new_quantity}")


    def product_sell(self, name, amount, cost):
        target_index = self.inventory.index[self.inventory['name'] == name]
        
        if target_index.empty:
            print(f"Error: Item {name} not found") 
            return
        idx = target_index[0]
        current_quantity = self.inventory.loc[idx, 'quantity']
        new_quantity = current_quantity - amount

        if new_quantity < 0:
            print("{name} new quantity is less than 0 operation cancelled")
            return

        self.inventory.loc[idx,'quantity'] = new_quantity
        print(f"Succesfully change {name} quantity to {new_quantity}")    





