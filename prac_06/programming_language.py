"""
Estimated time=20mins
Actual time=15mins
"""

"""Creating class"""
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    """returns True/False if the programming language is dynamically typed or not."""
    def is_dynamic(self):
        return self.typing.lower() == "dynamic"
    """adding __str__ method"""
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"