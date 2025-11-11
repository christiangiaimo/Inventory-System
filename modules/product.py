
class Product():
    def __init__(self,family,name,cost,unit,quantity):
        self.family = family
        self. name = name
        self.cost = cost
        self.unit = unit
        self.quantity = quantity



    def update_qty(self,new_qty):
        if type(new_qty) != int:
            raise ValueError("New quantity is not a valid number")
 
        else:
            self.quantity += new_qty


    def update_cost(self,new_cost):
        if type(new_cost) == int or type(new_cost) == float:
            self.cost = new_cost
        else:
            raise ValueError ("New cost is not a valid name")


    def update_name(self, new_name):
        if type(new_name != str):
            raise ValueError("New_name is not a valid name")
        else:
            self.name = new_name

    def update_unit(self, new_unit):
        if type(new_unit != str):
            raise ValueError("new_unit not a valid text")
        elif new_unit != "KG" or new_unit != "UND" or new_unit != "LT":
            raise ValueError("New unit not a valid unit")
        


