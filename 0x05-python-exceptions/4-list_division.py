#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            numby = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            numby = 0
        except (TypeError, ValueError):
            print("wrong type")
            numby = 0
        except (IndexError):
            print("out of range")
            numby = 0
        finally:
            div_list.append(numby)
    return div_list
