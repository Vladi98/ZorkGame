class Furniture:

    def __init__(self,name, info):
        self.name = name
        self.info = info
        self.items = []


    def set_info(self,value):
        self.info = value


    def show_info(self):
        print('This is a ' + self.name)
        print('It is made for: ' + self.info)