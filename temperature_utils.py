from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    return round((fahrenheit_temp - 32) * (5/9),2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    return round((celsius_temp * 9 / 5) + 32, 2)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    if input_unit_of_measurement == 'f':
        temp = []
        for i in temperatures:
            temp.append(convert_to_celsius(i))
        temps = tuple(temp)
        convert = zip(temperatures, temps)
        return tuple(convert)
    elif input_unit_of_measurement == 'c':
        temp = []
        for i in temperatures:
            temp.append(convert_to_fahrenheit(i))
        temps = tuple(temp)
        convert = zip(temperatures, temps)
        return tuple(convert)
    elif input_unit_of_measurement == 'a':
        temp = []
        for i in temperatures:
            temp.append(convert_to_kelvin(i))
            temps = tuple(temp)
            convert = zip(temperatures, temp)
            return tuple(convert)


def convert_to_kelvin(kelvin_temp: float) -> int:
    return round((kelvin_temp - 273.15) * (9 / 5 + 32))