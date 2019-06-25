from Commands import Commands
from Rooms import Room
from Basement import Basement
from Ceiling import Ceiling



class Parser:

    @staticmethod
    def parse(command):
        tokens = command.split()
        string=''
        for token in tokens:
            if(token not in Commands.list_of_commands):
                print('No verbs were found in this command! It is invalid!')
            elif token in Commands.list_of_commands:
                string+= ' '+token.name
            elif token in Room.items:
                string += ' '+token.name
            elif token in Ceiling.items:
                string += ' '+token.name
            elif token in Basement.items:
                string += ' '+token.name
        return string.split(' ')
    
print(Parser.parse('grab Axe'))