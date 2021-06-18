class Person:
    """Example implementation of a class"""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self) -> str:
        """Returns the Person's full name"""
        return f"{self.first_name} {self.last_name}"

    def hello(self) -> str:
        """Returns 'Hello, {first_name}'"""
        return f"Hello, {self.first_name}"
