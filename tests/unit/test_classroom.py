import pytest
import os
from src.classmap import Classroom, Pupil


def test_create_classroom():
    """Verify that creating a Classroom with specified rows and columns sets the correct shape."""
    classroom = Classroom(num_rows=5, num_columns=5)
    assert classroom.shape == (5, 5)


def test_shape_setter_invalid_rows():
    """Ensure setting an invalid number of rows (<= 0) raises a ValueError."""
    classroom = Classroom(3, 4)
    with pytest.raises(ValueError):
        classroom.shape = (0, 5)


def test_shape_setter_invalid_columns():
    """Ensure setting an invalid number of columns (<= 0) raises a ValueError."""
    classroom = Classroom(3, 4)
    with pytest.raises(ValueError):
        classroom.shape = (5, -1)


def test_add_pupil_accepts_string():
    """Check that add_pupil can accept a string name and creates a Pupil object with that name."""
    classroom = Classroom(2, 2)
    classroom.add_pupil("Alice")
    pupils = classroom.get_pupils()
    assert isinstance(pupils[0], Pupil)
    assert pupils[0].name == "Alice"


def test_add_pupil_accepts_pupil_instance():
    """Check that add_pupil can accept an existing Pupil instance."""
    classroom = Classroom(2, 2)
    p = Pupil("Bob")
    classroom.add_pupil(p)
    assert classroom.get_pupils()[0] is p


def test_display_map_position_conflict():
    """Verify that display_map raises ValueError if two pupils have the same position."""
    classroom = Classroom(2, 2)
    a = Pupil("A")
    b = Pupil("B")
    classroom.add_pupil(a)
    classroom.add_pupil(b)

    a.set_position(0, 0)
    b.set_position(0, 0)

    with pytest.raises(ValueError):
        classroom.display_map(filepath=os.path.join("tests", "data", "conflict_map.txt"))


def test_load_pupils_from_file():
    """Check that load_pupils_from_file correctly loads pupils from a text file."""
    classroom = Classroom(2, 3)
    classroom.load_pupils_from_file(os.path.join("tests", "data", "pupils_sample.txt"))
    names = [p.name for p in classroom.get_pupils()]
    assert names == ["Adam", "Blu", "Claire", "David", "Even", "Friedreich"]


def test_arrange_seating():
    """Ensure arrange_seating assigns unique positions to all pupils."""
    classroom = Classroom(2, 3)
    classroom.load_pupils_from_file(os.path.join("tests", "data", "pupils_sample.txt"))
    classroom.arrange_seating()
    
    positions: set[tuple[int, int]] = set()
    for pupil in classroom.get_pupils():
        pos = pupil.get_position()
        assert pos not in positions
        positions.add(pos)
        
    assert len(positions) == 6


def test_display_map():
    """Check that display_map runs without errors after seating arrangement."""
    classroom = Classroom(2, 3)
    classroom.load_pupils_from_file(os.path.join("tests", "data", "pupils_sample.txt"))
    classroom.arrange_seating()
    classroom.display_map(filepath=os.path.join("tests", "data", "classroom_map.txt"))


def test_arrange_seating_max_capacity():
    """Verify that pupils exceeding classroom capacity remain unseated after arrange_seating."""
    classroom = Classroom(1, 3)
    classroom.load_pupils_from_file(os.path.join("tests", "data", "pupils_sample.txt"))
    classroom.arrange_seating()

    seated = 0
    unseated = 0
    for p in classroom.get_pupils():
        try:
            p.get_position()
            seated += 1
        except ValueError:
            unseated += 1

    assert seated == 3
    assert unseated == 3


def test_display_map_creates_file(tmp_path: str):
    """Check that display_map creates a classroom_map.txt file in the specified directory."""
    file_path = os.path.join(tmp_path, "classroom_map.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
    
    classroom = Classroom(2, 2)
    classroom.add_pupil("A")
    classroom.add_pupil("B")
    classroom.arrange_seating()

    cwd = os.getcwd()
    os.chdir(tmp_path)
    file_path = os.path.join(tmp_path, "classroom_map.txt")
    classroom.display_map(filepath=file_path)
    assert os.path.exists(file_path)
    os.chdir(cwd)