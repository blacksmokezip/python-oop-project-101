from validator.main import Validator


v = Validator()

schema = v.dict()

schema.shape({
    "name": v.string().required(),
    "age": v.number().positive(),
})

negative_num = -7
positive_num = 22
empty = ""
name = "Frank"


def test_validation():
    assert schema.is_valid({'name': name, 'age': positive_num}) is True
    assert schema.is_valid({'name': name, 'age': None}) is True
    assert schema.is_valid({'name': empty, 'age': None}) is False
    assert schema.is_valid({'name': name, 'age': negative_num}) is False