import pytest

from boilerplate.examples.classes import Person


@pytest.fixture(scope="function")
def alice():
    """Returns a sample instance of the Person which gets recreated
    for every pytest function. This instance has the following attributes:
        first_name: Alice
        last_name: Doe
        age: 35
    """
    return Person("Alice", "Doe", 35)
