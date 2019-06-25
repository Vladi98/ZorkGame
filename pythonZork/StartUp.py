from Floors import Floor
from Commands import Commands
from Inventory import Inventory
from Rooms import Room
from Items import Items
from Basement import Basement
from Menu import Menu
from Player import Player
from StorageRoom import StorageRoom
from RestingRoom import RestingRoom
from Parser import Parser
from sys import exit




p = Player('Vladimir')
Menu.action()


storageRoom =StorageRoom('Storageroom','Resting room')
restingRoom =RestingRoom('Storageroom','Resting room')
basement = Basement('Basement',storageRoom)

storageRoom.add_items()
basement.add_items()
currentRoom = basement
currentRoom.show_info()
command = input()
while True:
    parsed_command = Parser.parse(command)
    tokens = parsed_command.split(' ')
   #tokens = Parser.parse(command)

    #if currentRoom == storageRoom:
     #   if tokens[0] == 'exit':
    #        break

    if tokens[0] == 'go' and tokens[1] == 'next':
        if currentRoom.has_door() and currentRoom.open_door():
            currentRoom = currentRoom.links
            currentRoom.show_info()

        else:
            print("You can not proceed to the next room. You should open the door first")


    elif tokens[0] == 'drop':
            item_to_drob = tokens[1]
            p.drop_item(item_to_drob)


    elif tokens[0] == 'grab':
            item_to_grab = tokens[1]
            p.grab_item(item_to_grab,currentRoom)



    elif tokens[0] == 'open':
        if tokens[1] == 'door':
            if currentRoom.open_door():
                print('Where do you want to go from here')

                    

    elif tokens[0] == 'show':
        if tokens[1] == 'inventory':
            p.inventory.show_items()

    elif tokens[0] == 'inspect':
        for item in currentRoom.items:
            if tokens[1] == item.name:
                 print(item.show_info())
        
      

    command= input()












