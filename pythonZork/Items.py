class Items:
    
    def __init__(self,name,info):
        self.name = name
        self.info = info

    def get_name(self):
        return self.name

    def set_name(self,value):
        self.name = value

    def show_info(self):
        print(self.info)
