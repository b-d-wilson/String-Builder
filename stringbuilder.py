"""Implementation of a StringBuilder"""


class StringBuilder():
    """Builds a string"""

    def __init__(self, delimiter: str = '') -> None:
        self.delimiter = delimiter
        self.charlist = []

    def append(self, word: str) -> None:
        self.charlist += list(word)

    def to_string(self) -> str:
        self.delimiter.join(self.charlist)

