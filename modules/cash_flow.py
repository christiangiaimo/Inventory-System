import pandas as pd
import os


path = "/home/cgiaimo/Desktop/workspace/github.com/christiangiaimo/Inventory-System/data"
name_file='cash_flow_data.json'
full_path = os.path.join(path,name_file)


class Cash_Flow():
    def __init__(self):
        self.full_path = full_path
        self.cash_flow = self.load_cash_flow_json()
       
        
    def add_income(self,amount):

        self.cash_flow.iloc[0,0] += amount
        self.cash_flow.iloc[0,-1] += amount
        
    
    def add_expense(self,amount):
        self.cash_flow.iloc[0,1] += amount
        self.cash_flow.iloc[0,-1] -= amount
        
        

    def load_cash_flow_json(self):
        if os.path.exists(self.full_path):
            df = pd.read_json(self.full_path,orient='records')
            return df
        else:
            print("Cash flow not found, creating a new cash flow file")
            df =  pd.DataFrame({'income':[0],
                                'expense':[0],
                                'total':[0]})
            return df
            

    def export_cash_flow_json(self):
        self.cash_flow.to_json(self.full_path, orient ="records", indent=4)        
           