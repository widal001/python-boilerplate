"""Test that the package was installed correctly."""

import boilerplate


def test_package_named_correctly():
    """The package should be imported and named correctly."""
    assert boilerplate.__name__ == "boilerplate"
