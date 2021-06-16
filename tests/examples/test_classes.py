import pytest

from boilerplate.examples import Person


@pytest.mark.parametrize("name", ["Joe Biden", "Kamala Harris"])
def test_person(name):
    # execution
    p = Person(name)
    # validation
    assert p.name == name
