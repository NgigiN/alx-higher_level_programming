#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(coutn))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i+1]))
