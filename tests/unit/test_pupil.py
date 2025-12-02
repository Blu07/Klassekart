from src.classmap import Pupil

def test_create_pupil():
    pupil = Pupil(name="John Doe", age=10)
    assert pupil.name == "John Doe"
    assert pupil.age == 10
