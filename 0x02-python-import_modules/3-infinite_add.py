#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    from  sys import argv

    a = 10
    b = 5
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
        print("{:d}".format(sum))
