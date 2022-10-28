#Created by Connor Harris
from guizero import App, Text, PushButton, Window
import single_player

#The functions for pressing buttons to access alt menus
def open_single_match():
    app.hide()
    single_match_window.show()

def close_single_match():
    single_match_window.hide()

def open_tournament_match():
    tour_match_window.show()

def close_tournament_match():
    tour_match_window.hide()

def open_single_player():
    single_match_window.hide()
    #single_player_window.show()
    single_player.start_game()

def close_single_player():
    single_player_window.hide()

def open_two_player():
    single_match_window.hide()
    two_player_window.show()

def close_two_player():
    two_player_window.hide()

def open_main_app():
    app.show()
    two_player_window.hide()
    single_match_window.hide()
    tour_match_window.hide()
    single_player_window.hide()


def exit_game():
    app.destroy()

def exit_single_player():
    single_player_window.hide()

def exit_two_player():
    two_player_window.hide()

# def open_single_match():


#Application Screens
app = App(title="SE Project - Menu Prototype")
single_match_window = Window(app, title="Single Match")
tour_match_window = Window(app, title="Tournament Match")
single_player_window = Window(single_match_window, title="Single player mode (Player vs AI)")
two_player_window = Window(single_match_window, title="Two player mode (Player 1 vs Player 2)")

#Top of main screen messages
message_1 = Text(app, text="Welcome to the app!")
message_2 = Text(app, text="Please select an option:")

#Interactive buttons in the main screen window
main_screen_select_singlematch = PushButton(app, command=open_single_match, text="Single Match")
main_screen_select_tournament = PushButton(app, command=open_tournament_match, text="Tournament")
ain_screen_select_exit = PushButton(app, command=exit_game, text="exit")

#Interactive buttons in the Single Match alt screen
singlematch_screen_single_player = PushButton(single_match_window, command=open_single_player, text="Single Player: Player vs AI")
singlematch_screen_multi_player = PushButton(single_match_window, command=open_two_player, text="Multi Player: Player 1 vs Player 2")
singlematch_screen_back_menu = PushButton(single_match_window, command=open_main_app, text="Go Back")
singlematch_screen_exit = PushButton(single_match_window, command=exit_game, text="Exit")


tournament_screen_player = PushButton(tour_match_window, command=exit_game, text="Exit")
exit_single_player = PushButton(single_player_window, command=exit_game, text="Exit")
exit_two_player = PushButton(two_player_window, command=exit_game, text="Exit")

#Hide all windows to start with, except the main one
single_player_window.hide()
two_player_window.hide()
tour_match_window.hide()
single_match_window.hide()
app.display()