# Create a calculator class with methods for adding and multiplication

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value += value

    def multiply(self, value):
        self.value *= value

    def clear(self):
        self.value = 0

    def get_value(self):
        return self.value
    