from validator.main import Validator


schema = Validator().number()

negative_seven = -7
positive_nine = 9


def test_no_requirements():
    assert schema.is_valid() is True
    assert schema.is_valid(negative_seven) is True


def test_required():
    assert schema.required().is_valid() is False
    assert schema.is_valid(positive_nine) is True
    assert schema.is_valid() is False


def test_positive():
    assert schema.positive().is_valid(negative_seven) is False
    assert schema.positive().is_valid(positive_nine) is True


def test_range():
    schema.range(-5, 10)
    assert schema.is_valid(negative_seven) is False
    assert schema.is_valid(positive_nine) is True
    schema.range(1, 2)
    assert schema.is_valid(positive_nine) is False
