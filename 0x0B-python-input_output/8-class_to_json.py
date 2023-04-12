#!/usr/bin/python3

def class_to_json(obj):
    for attr, value in obj.__dict__.items():
        if isintance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
