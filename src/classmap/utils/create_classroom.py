import os
from models import Classroom
from .input_validation import get_postive_int


def create_classroom_from_file():
    pupils_filepath: str = os.path.join("input_data", "pupils.txt")
    classroom_filepath: str = os.path.join("input_data", "classroom.txt")

    # Create a Classroom instance from given dimensions in file
    with open(classroom_filepath, 'r') as file:
        # First line contains num_rows and second contains num_columns
        num_rows = int(file.readline().strip())
        num_columns = int(file.readline().strip())

        classroom = Classroom(num_rows=num_rows, num_columns=num_columns)

    # Load pupils from file
    classroom.load_pupils_from_file(pupils_filepath)

    return classroom


def create_classroom_from_console():
    # Ask for classroom dimensions and create Classroom instance
    num_rows: int = get_postive_int("Enter number of rows in the classroom: ")
    num_columns: int = get_postive_int(
        "Enter number of columns in the classroom: ")

    classroom = Classroom(num_rows=num_rows, num_columns=num_columns)

    print("Enter pupil names one at a time. Leave blank to indicate an empty seat.")

    capacity = num_rows * num_columns
    count = 0
    while count < capacity:
        name = input("Enter pupil name: ")

        # Empty names are empty seats. Skip adding pupil, but count towards capacity.
        if name.strip() == "":
            count += 1
            continue

        classroom.add_pupil(name)
        count += 1

    return classroom
