#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)
        if value < previous_value:
            result -= value
        else:
            result += value
        previous_value = value
    return result
