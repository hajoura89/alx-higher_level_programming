#!/usr/bin/python3
# Print the addition of all arguments.
if __name__ == "__main__":
    import sys

    somme = 0
    for i in range(len(sys.argv) - 1):
        somme += int(sys.argv[i + 1])
    print("{}".format(somme))
