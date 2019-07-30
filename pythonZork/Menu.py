from Commands import Commands
from Player import Player
from sys import exit


class Menu:

    @staticmethod
    def show_menu():
        print('Main menu of the game: ')
        print('Play - starts the game')
        print('Help - view all the commands')
        print('Exit - closes the application')
        
    @staticmethod
    def show_commands():
        print('The commands you can use are: ')
        print(Commands.list_of_commands)

    @staticmethod
    def about_player():
        print (Player.show_info())

    def action():
        print("Type About to view menu")
        command = input()
        while True:
            command = command.lower()
            if command == 'exit':
                exit(0)
        
            elif command == 'help':
                Menu.show_commands()

            elif command == 'about':
                Menu.show_menu()

            elif command == 'play':
                print('Starting game..')
                break

            command = input()
      