# Excercise: https://www.hackinscience.org/exercises/temperature-class
#
#
# Solution:

class Temp_converter:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        match self.public_name:
            case "kelvin":
                return obj.default_value
            case "celsius":
                return obj.default_value - 273.15
            case "fahrenheit":
                return  obj.default_value * 9 / 5 - 459.67

    def __set__(self, obj, value):
        match self.public_name:
            case "kelvin":
                obj.default_value = value
            case "celsius":
                obj.default_value = value + 273.15
            case "fahrenheit":
                obj.default_value = (value + 459.67) * 5 / 9


class Temperature:

    kelvin = Temp_converter()
    celsius = Temp_converter()
    fahrenheit = Temp_converter()

    def __init__(self):
        default_value: float = 0



if __name__ == "__main__":
    t1 = Temperature()
    t1.celsius = 0
    print(t1.kelvin)
    print(t1.fahrenheit)