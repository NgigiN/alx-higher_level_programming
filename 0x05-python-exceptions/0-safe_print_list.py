#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    final = 0
    for i in range(x):
		try:
			print("{}".format(my_list[i]), end='')
			final = final + 1
    	except IndexError:
       		break
    print("")
    return (total)
