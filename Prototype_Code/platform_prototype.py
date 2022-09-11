#Created by Connor Harris
from guizero import App, Text, PushButton, Window

#The functions for pressing buttons to access alt menus
def open_single_player():
    single_player_window.show()

def close_single_player():
    single_player_window.hide()

def open_two_player():
    two_player_window.show()

def close_two_player():
    two_player_window.hide()

def exit_game():
    app.destroy()

def exit_single_player():
    single_player_window.hide()

def exit_two_player():
    two_player_window.hide()

#Application Screens
app = App(title="SE Project - Menu Prototype")
single_player_window = Window(app, title="Single player mode")
two_player_window = Window(app, title="Single player mode")

#Top of main screen messages
message_1 = Text(app, text="Welcome to the app!")
message_2 = Text(app, text="Please select an option:")

#Interactive buttons in the main screen window
main_screen_select_singleplayer = PushButton(app, command=open_single_player, text="Single player")
main_screen_select_two_player = PushButton(app, command=open_two_player, text="Two player")
ain_screen_select_exit = PushButton(app, command=exit_game, text="exit")

#Interactive buttons in the two alt screens
exit_single_player = PushButton(single_player_window, command=exit_single_player, text="Exit")
exit_two_player = PushButton(two_player_window, command=exit_two_player, text="Exit")

#Hide all windows to start with, except the main one
single_player_window.hide()
two_player_window.hide()
app.display()