from validator.main import Validator


schema1 = Validator().string()
schema2 = Validator().string()

empty = ""
four_symbols = "Four"
ten_symbols = "TenSymbols"


def test_no_requirements():
    assert schema1.is_valid() is True
    assert schema1.is_valid(empty) is True
    assert schema1.is_valid(four_symbols) is True


def test_required():
    assert schema1.required().is_valid() is False
    assert schema1.is_valid(empty) is False
    assert schema1.is_valid(four_symbols) is True
    assert schema2.is_valid() is True


def test_min_len():
    assert schema2.min_len(4).is_valid() is False
    assert schema2.min_len(4).is_valid(four_symbols) is True
    assert schema2.min_len(11).is_valid(ten_symbols) is False


def test_contains():
    assert schema1.contains("something").is_valid() is False
    assert schema1.contains("Four").is_valid(four_symbols) is True
    assert schema1.contains("Five").is_valid(ten_symbols) is False
