from turtle import Turtle


def get_coordinates(province, dataframe):
    """Returns the x and y coordinates for a province from a pandas dataframe."""
    current_province_data = dataframe[dataframe.iso_nombre == province]
    current_province_coordinates = (
        float(current_province_data.x_coord),
        float(current_province_data.y_coord),
    )
    return current_province_coordinates


class Board(Turtle):
    """The board to write the provinces names on the map."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct_answers = []
        self.missing_provinces = []

    def write_province(self, province: str, coordinates: tuple) -> None:
        """Write the province name on the given x and y coordinates."""
        self.goto(coordinates)
        self.write(arg=province, align="left")
        self.correct_answers.append(province)

    def list_missing(self, all_provinces: list):
        """Returns a list of all missing provinces."""
        self.missing_provinces = [province for province in all_provinces
                                  if province not in self.correct_answers]
        return self.missing_provinces
