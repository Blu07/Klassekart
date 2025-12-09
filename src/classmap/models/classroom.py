from .pupil import Pupil
from random import choice


class Classroom:
    def __init__(self, num_rows: int, num_columns: int):
        self._pupils: list[Pupil] = []
        self._num_rows = num_rows
        self._num_columns = num_columns

    @property
    def shape(self) -> tuple[int, int]:
        return (self._num_rows, self._num_columns)

    @shape.setter
    def shape(self, value: tuple[int, int]) -> None:
        """
        Set the shape of the classroom by specifying the number of rows and columns.

        :param rows: The desired number of rows in the classroom
        :type rows: int
        :param columns: The desired number of columns in the classroom
        :type columns: int
        """

        rows, columns = value

        if rows <= 0:
            raise ValueError("Number of rows must be a positive integer.")
        if columns <= 0:
            raise ValueError("Number of columns must be a positive integer.")

        self._num_rows = rows
        self._num_columns = columns

    def add_pupil(self, pupil: Pupil | str) -> None:
        """
        Add a pupil to the classroom.

        :param pupil: The pupil to add (either a Pupil instance or a name string)
        :type pupil: Pupil | str
        """

        # If a string is provided, create a Pupil instance
        if isinstance(pupil, str):
            pupil = Pupil(name=pupil)

        self._pupils.append(pupil)

    def get_pupils(self) -> list[Pupil]:
        """
        Get the list of pupils in the classroom.

        :return: List of pupils
        :rtype: list[Pupil]
        """
        return self._pupils

    def arrange_seating(self) -> None:
        """
        Arrange random seating for all pupils in the classroom.

        """

        # Go through each position row by row, column by column
        # Choose a random pupil to be seated at the current position

        pupils_not_seated = self._pupils.copy()

        for row in range(self._num_rows):
            for col in range(self._num_columns):

                # All pupils are seated
                if not pupils_not_seated:
                    return

                # Select a random pupil who is not yet seated
                pupil_to_be_seated = choice(pupils_not_seated)
                pupil_to_be_seated.set_position(row, col)
                pupils_not_seated.remove(pupil_to_be_seated)

    def display_map(self, filepath: str = "classroom_map.txt", printout: bool = False) -> None:
        """
        Create a 2D array representing the classroom layout.
        Pretty print the classroom map with pupils' positions.

        :param filepath: The file path to save the classroom map to
        :type filepath: str
        :param printout: Whether to print the classroom map to the console or not
        :type printout: bool
        """

        # Initialize empty classroom array
        classroom_array: list[list[str | None]] = [
            [None for _ in range(self._num_columns)] for _ in range(self._num_rows)]

        # Fill the array with pupil names based on their positions
        for pupil in self._pupils:
            # Skip pupils without a set position
            try:
                row, col = pupil.get_position()
            except ValueError:
                continue

            # Check for position conflicts
            if (occupant := classroom_array[row][col]) is not None:
                raise ValueError(
                    f"Position ({row}, {col}) is already occupied by {occupant} trying to add pupil {pupil.name}.")

            # Place pupil in the classroom array
            classroom_array[row][col] = pupil.name

        # Print the layout in a readable format

        # Set the number of characters per column to the longest name + padding
        width: int = 1 + max((len(p.name)
                             for p in self._pupils), default=5) + 1

        # Write to file and optionally print to console
        with open(filepath, "w") as file:
            for row in classroom_array:
                row_display: list[str] = ["| "]

                for pupil_name in row:
                    if pupil_name is None:
                        row_display.append(f"{'=====':^{width}} | ")
                    else:
                        row_display.append(f"{pupil_name:^{width}} | ")

                file.write(" ".join(row_display).ljust(width) + "\n")

                if printout:
                    print(" ".join(row_display).ljust(width))

    def load_pupils_from_file(self, filepath: str) -> None:
        """
        Load pupils from a file and add them to the classroom.

        :param filepath: Description
        :type filepath: str
        """

        with open(filepath, 'r') as file:
            # File contains one name per line, no headers and no extra characters
            loaded_pupil_names = [line.strip() for line in file.readlines()]

            for name in loaded_pupil_names:
                self.add_pupil(name)
