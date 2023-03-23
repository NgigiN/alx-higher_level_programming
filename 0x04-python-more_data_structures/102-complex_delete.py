#!/usr/bin/python3
def complex_delete(my_dict, value):
    victims = []
    for key in my_dict:
        if my_dict[key] == value:
            victims.append(key)
    for key in victims:
        del mydict[key]
    return my_dict
