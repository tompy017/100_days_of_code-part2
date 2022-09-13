"""Argentina's Provinces Game.
Project for Angela Wu's 100 days of code challenges.
"""
import sys
import turtle
import pandas
from fun_and_board import Board, get_coordinates

# Screen setups
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#9ddeda")
screen.title("How many Provinces of Argentina do you know?")  # Window title
map_img = "Argentina700.gif"  # PATH to image
screen.addshape(map_img)
turtle.shape(map_img)

data = pandas.read_csv("prov_args.csv")  # Pandas Dataframe
provinces_list = data.iso_nombre.to_list()

board = Board()

while len(board.correct_answers) < len(provinces_list):
    player_guess = screen.textinput(
        title=f"{len(board.correct_answers)}/{len(provinces_list)} - Guess a province",
        prompt="Enter the name of a province."
    )
    # Exit game and save all missing prov on a csv file
    if player_guess.lower() == "exit":
        missing_prov = board.list_missing(all_provinces=provinces_list)
        new_file = pandas.Series(missing_prov).to_csv("provinces_to_learn.csv")
        break

    for province in provinces_list:
        try:
            if province.lower() == player_guess:
                coordinates = get_coordinates(province=province, dataframe=data)
                board.write_province(province=province, coordinates=coordinates)
        # If user cancels input will raise AttributeError - None.lower()
        except AttributeError:
            sys.exit()
