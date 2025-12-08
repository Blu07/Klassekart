
from models.classroom import Classroom
from utils.input_validation import get_postive_int

def main():
    
    # Ask for classroom dimentions
    num_rows: int = get_postive_int("Enter number of rows in the classroom: ")
    num_columns: int = get_postive_int("Enter number of columns in the classroom: ")

    classroom = Classroom(num_rows=num_rows, num_columns=num_columns)
    
    print("Enter pupil names one at a time. Type 'exit' to finish.")
    
    count = 0
    while count < (num_rows * num_columns):
        name = input("Enter pupil name: ")
        if name.lower() == 'exit':
            break
        
        # Empty names are empty seats. Skip adding pupil, but count towards capacity.
        if name.strip() == "":
            count += 1
            continue
        
        classroom.add_pupil(name)
        count += 1
    
    classroom.arrange_seating()
    classroom.display_map(filepath="classroom_map.txt", printout=True)
    print("Classroom map saved to 'classroom_map.txt'.")



if __name__ == "__main__":
    main()