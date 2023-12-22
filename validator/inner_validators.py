class StringValidator:
    """Validates 'str' type data"""

    req: bool  # Not None or empty data required
    length: int  # Minimum length of string
    data: str  # String must contain this data

    def __init__(self, req=False, length=0, data=""):
        self.req = req
        self.length = length
        self.data = data

    def required(self):
        """Sets 'Required' parameter value to 'True'"""

        self.req = True
        return self.__class__(req=True, length=self.length, data=self.data)

    def min_len(self, length):
        """Sets minimum length"""

        self.length = length
        return self.__class__(req=self.req, length=length, data=self.data)

    def contains(self, data):
        """Sets data that string must contain"""

        self.data = data
        return self.__class__(req=self.req, length=self.length, data=data)

    def is_valid(self, data=None):
        """Checks if string is valid"""

        if self.req:
            if data is None or not data:
                return False

        if data is None:
            if self.data or self.length > 0:
                return False
            return True

        if len(data) < self.length:
            return False

        if self.data not in data:
            return False
        return True


class NumberValidator:
    """Validates 'int' type data"""

    req: bool  # Not None data required
    is_positive: bool  # Number must be positive
    range_: tuple  # Number must be in this range

    def __init__(self, req=False, positive=False, range_=None):
        self.req = req
        self.is_positive = positive
        self.range_ = range_

    def required(self):
        """Sets 'Required' parameter value to 'True'"""

        self.req = True
        return self.__class__(req=True, positive=self.is_positive, range_=self.range_)

    def positive(self):
        """Sets 'Positive' parameter value to 'True'"""

        self.is_positive = True
        return self.__class__(req=self.req, positive=True, range_=self.range_)

    def range(self, min_, max_):
        """Sets range that must contain data"""

        self.range_ = (min_, max_)
        return self.__class__(req=self.req, positive=self.is_positive, range_=(min_, max_))

    def is_valid(self, data=None):
        """Checks if number is valid"""

        if self.req:
            if data is None:
                return False
        elif data is None:
            return True

        if self.is_positive:
            if data < 0:
                return False

        if self.range_:
            if data < self.range_[0] or data > self.range_[1]:
                return False

        return True


class ListValidator:
    """Validates 'list' type data"""

    req: bool
    size: int

    def __init__(self, req=False, size=None):
        self.req = req
        self.size = size

    def required(self):
        """Sets 'Required' parameter value to 'True'"""
        self.req = True
        return self.__class__(req=True, size=self.size)

    def sizeof(self, size):
        """Sets the required size of list"""

        self.size = size
        return self.__class__(req=self.req, size=size)

    def is_valid(self, data=None):
        """Checks if list is valid"""

        if self.req:
            if not isinstance(data, list):
                return False

        if self.size:
            if len(data) != self.size:
                return False

        return True


class DictValidator:
    """Validates 'dict' type data"""

    shape_: dict

    def __init__(self, shape_=None):
        self.shape_ = shape_

    def shape(self, shape_):
        """Sets the requirements for validation"""

        self.shape_ = shape_
        return self.__class__(shape_=shape_)

    def is_valid(self, data):
        """Checks if dict is valid"""

        if not self.shape_:
            return False

        for key, value in data.items():
            if not self.shape_[key].is_valid(value):
                return False

        return True
