class Bill:
    def __init__(self, name, value, paid=False):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} :{self.value}"
    