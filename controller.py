import exceptions

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok")
        except:
            print("Problem")