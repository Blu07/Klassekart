import os
from models import Classroom
from utils import create_classroom_from_file, create_classroom_from_console

def main():
    classroom: Classroom
    
    save_filepath = os.path.join("results", "classroom_map.txt")
    
    # Ask whether to load pupils and classroom dimensions from file or manually
    read_from_file_or_manual = input("Load pupils from file? (y/n): ").strip().lower()
    
    # Create classroom based on user choice
    if read_from_file_or_manual == 'y': classroom = create_classroom_from_file()
    else: classroom = create_classroom_from_console()
    
    # Arrange seating and display map
    classroom.arrange_seating()
    classroom.display_map(filepath=save_filepath, printout=True)
    print(f"Classroom map saved to {save_filepath}")



if __name__ == "__main__":
    main()