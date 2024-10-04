class OutOfStock(Exception):
    def __init__(self, item_name):
        self.item_name = item_name
        
    def __str__(self):
        return f"Sorry {self.item_name} is currently unavailbale, please check again in the next 24 hours"
    
october_inventory = {
        
        "apple": 200,
        "mango": 100,
        "orange": 0
    }

def purchase_item():
    
    print("here is the list of fruits to choose from: ")
    print("orange, mango, apple")
    
    item = input("Enter the name of the fruit you wish yo buy:")
    quantity = int(input("please enter the quantity you wnat to purchase: "))
    
    try:
       if october_inventory[item] == 0:
           raise OutOfStock(item)
       else:
           print(f"Purchase successful: {quantity} {item}(s)")
           october_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry '{item}' is not availbale in our inventory")
        
purchase_item()
    