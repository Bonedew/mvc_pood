import exceptions

#represents shop structure
#list of Product type objects
items = []

#add item to items
def addItem(name, price, amount):
    global items
    #create product with required descriptions
    product = Product(name, price, amount)
    items.append(product)
    if product in items:
        raise exceptions.itemExists("Item {} already exists".format(name))
    else:
        items.append(product)