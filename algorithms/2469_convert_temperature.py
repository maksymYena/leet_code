from typing import List


def convertTemperature(celsius: float) -> List[float]:
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.80) + 32
    return kelvin, fahrenheit


print(convertTemperature(36.5))