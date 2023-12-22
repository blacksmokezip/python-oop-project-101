from validator.main import Validator


schema = Validator().list()

empty = []
two_elements = [1, 2]
five_elements = [1, 2, 3, 4, 5]


def test_no_requirements():
    assert schema.is_valid() is True
    assert schema.is_valid(two_elements) is True


def test_required():
    assert schema.required().is_valid() is False
    assert schema.is_valid() is False
    assert schema.is_valid(empty) is True


def test_sizeof():
    schema.sizeof(2)
    assert schema.is_valid(empty) is False
    assert schema.is_valid(two_elements) is True
    assert schema.is_valid(five_elements) is False
