import pytest
from classmap.models import Pupil

def test_create_pupil():
    pupil = Pupil(name="John Doe")
    assert pupil.name == "John Doe"


def test_set_position():
    pupil = Pupil(name="Jane Doe")
    
    # Set valid position
    pupil.set_position(2, 3)
    assert pupil.get_position() == (2, 3)


def test_get_position_not_set():
    pupil = Pupil(name="John Doe")
    
    # Position should be (None, None) initially
    with pytest.raises(ValueError):
        pupil.get_position()


def test_get_position_valid():
    pupil = Pupil(name="Jane Doe")
    pupil.set_position(2, 3)
    
    # Get position
    assert pupil.get_position() == (2, 3)