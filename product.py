# product.py
class Product:
    # construct
    def __init__(self, name, price, amount):
        self.setName(name)
        self.setPrice(price)
        self.setAmount(amount)
    #product test view
    def __repr__(self):
        return "name: {} \n price: {} \n amount: {}".format(self.getName(), self.getPrice(), self.getAmount())
    # setters
    def setName(self, name):
        self.__name = name
    def setPrice(self, price):
        self.__price = price
    def setAmount(self, amount):
        self.__amount = amount
    #gettest
    def getName(self, name):
        self.__name = name
    def getPrice(self, price):
        self.__price = price
    def getAmount(self, amount):
        self.__amount = amount