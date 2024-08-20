class Bicycle:
    """
    A bicycle with some attributes and methods

    Attributes
    ----------
    _type: str
    _size: int
    _color: str
    """

    def __init__(self, type='mountainbike', size=48):
        """
        Konstruktor initialisiert das Objekt mit 3 Parameterwerten.
        """
        self._type = type
        self._size = size
        self._color = 'gray'

    @property
    def type(self):
        """
        Liefert den Typ des Fahrrads
        """
        return self._type

    @property
    def size(self):
        """
        Liefert die Grösse des Fahrrads
        """
        return self._size

    @property
    def color(self):
        """
        Liefert die Farbe des Fahrrads
        """
        return self._color

    @type.setter
    def type(self, type):
        """
        Legt den Typ des Fahrrads fest
        """
        self._type = type

    @size.setter
    def size(self, size):
        """
        Legt die Grösse des Fahrrads fest
        """
        self._size = size

    @color.setter
    def color(self, color):
        """
        Legt die Farbe des Fahrrads fest
        """
        self._color = color

    def print(self):
        """
        prints a human-readable representation of the object
        :return:
        """
        print(
            f'Fahrrad:\n'
            f'\tArt:            {self._type}\n'
            f'\tRahmengrösse:   {self._size}\n'
            f'\tFarbe:          {self._color}'
        )


if __name__ == "__main__":
    # Aufgabe 1
    bicycle = Bicycle()
    bicycle.print()
    #
    bicycle = Bicycle(type='racebike')
    bicycle.print()
    #
    bicycle = Bicycle(type='citybike', size='42')
    bicycle.print()
    #
    # Aufgabe 2
    #
    bicycle.color = 'red'
    bicycle.print()
