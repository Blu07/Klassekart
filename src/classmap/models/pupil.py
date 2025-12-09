class Pupil:
    """
    Represents a pupil with a name and position in a classroom as (row, column).
    """

    def __init__(self, name: str):
        """
        Initialize a Pupil with a name. Position is set later by Classroom.

        :param name: The name of the pupil
        :type name: str
        """
        self.name: str = name
        self._row: int | None = None
        self._column: int | None = None

    def set_position(self, row: int, column: int) -> None:
        """
        Set the position of the pupil in the classroom.
        Position below zero are rejected.
        Positive integer validation is done in Classroom.

        :param row: The row position of the pupil
        :type row: int
        :param column: The column position of the pupil
        :type column: int
        """

        self._row = row
        self._column = column

    def get_position(self) -> tuple[int, int]:
        """
        Get the position of the pupil if set.

        :return: The (row, column) position of the pupil
        :rtype: tuple[int, int]
        """

        # Validate that position is set before returning
        if self._row is None:
            raise ValueError("Row not set for this pupil.")

        if self._column is None:
            raise ValueError("Column not set for this pupil.")

        return self._row, self._column

    def __repr__(self):
        return f"Pupil(name={self.name}, row={self._row}, col={self._column})"
