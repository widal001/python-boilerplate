import pytest

from boilerplate.examples.classes import Person


class TestPerson:
    """Tests for the Person class"""

    @pytest.mark.parametrize(
        "first_name, last_name, age",
        [
            ("Joe", "Biden", 78),
            ("Kamala", "Harris", 56),
        ],
    )
    def test_init(self, first_name, last_name, age):
        """Tests __init__() for Person and validates that:
        - All of the init parameters match class attributes
        - The value of self.full_name is the concatenation of first_name
          and last_name with a space between
        """
        # setup
        full = f"{first_name} {last_name}"
        # execution
        person = Person(first_name, last_name, age)
        # validation
        assert person.full_name == full
        assert person.age == age
        assert person.first_name == first_name
        assert person.last_name == last_name

    def test_hello(self, alice):
        """Tests the hello() method and validates that:
        - It returns 'Hello, {Person.first_name}'
        """
        # setup
        expected = "Hello, Alice"
        # execution
        greeting = alice.hello()
        # validation
        assert greeting == expected
