import json
def get_products()-> list: #->list подсказка
    with open("db.json") as file:
        products = json.load(file)
    return products

def update_products(products:list): #:list подсказка
    with open("db.json" ,"w") as file:
        json.dump(products,file)
