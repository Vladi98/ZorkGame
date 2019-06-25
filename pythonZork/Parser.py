from Commands import Commands
from Rooms import Room
from Basement import Basement
from Ceiling import Ceiling
from StorageRoom import StorageRoom
from RestingRoom import RestingRoom
from KidsRoom import KidsRoom



class Parser:

    @staticmethod
    def parse(command):

        b = Basement('Basement','Storage')
        s = StorageRoom('StorageRoom','Resting Room')
        r = RestingRoom('RestingRoom','Kids Room')
        k = KidsRoom('KidsRoom','')
        b.add_items()
        s.add_items()
     


        tokens = command.split()
        string=''
        for token in tokens:
            if(token in Commands.list_of_commands):
                string+= token

            if token == 'door':
                string+= ' '+token
                return string

            elif token == 'inventory':
                string+= ' '+token
                return string

            for item in b.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in s.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in r.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in b.items:
                if item.name == token:
                    string+=' ' +token
                    return string
            
        return 'Not a valid command! Try again'
    
print(Parser.parse('open thew door axe solid'))