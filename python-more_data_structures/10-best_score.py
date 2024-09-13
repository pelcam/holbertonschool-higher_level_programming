#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    max_value = float('-inf')
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key
    return best_key
