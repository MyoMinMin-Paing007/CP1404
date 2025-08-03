"""Band class for CP1404 - demonstrating association (Band has Musicians)."""


class Band:
    """Band class represents a group of musicians."""

    def __init__(self, name=""):
        """
        Construct a Band with a name and an empty list of musicians.

        :param name: str - Name of the band
        """
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the band and its members."""
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def add(self, musician):
        """
        Add a musician to the band.

        :param musician: Musician - an instance of the Musician class
        """
        self.members.append(musician)

    def play(self):
        """
        Return a string showing each band member playing their instrument.

        :return: str - One line per member
        """
        return "\n".join(member.play() for member in self.members)