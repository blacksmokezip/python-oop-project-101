from validator.inner_validators import StringValidator, NumberValidator, ListValidator


class Validator:
    """Validates data"""

    class string(StringValidator):
        pass

    class number(NumberValidator):
        pass

    class list(ListValidator):
        pass
