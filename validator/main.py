class Validator:

    class string:
        req: bool
        length: int
        data: str

        def __init__(self, req=False, length=0, data=""):
            self.req = req
            self.length = length
            self.data = data

        def required(self):
            self.req = True
            return self.__class__(req=True, length=self.length, data=self.data)

        def min_len(self, length):
            self.length = length
            return self.__class__(req=self.req, length=length, data=self.data)

        def contains(self, data):
            self.data = data
            return self.__class__(req=self.req, length=self.length, data=data)

        def is_valid(self, data=None):
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
