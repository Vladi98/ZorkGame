from Commands import Commands
from Rooms import Room
from Basement import Basement
from Ceiling import Ceiling
from Closet import Closet
from Hallway import Hallway
from FinalRoom import FinalRoom
from StorageRoom import StorageRoom
from RestingRoom import RestingRoom
from KidsRoom import KidsRoom



class Parser:

    @staticmethod
    def parse(command):

        b = Basement('Basement')
        s = StorageRoom('StorageRoom')
        r = RestingRoom('RestingRoom')
        #k = KidsRoom('KidsRoom','')
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

            if token == 'next':
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
    
