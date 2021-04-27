import sys

def main(message, number):
    print(message + str(number))

main(sys.argv[1], sys.argv[2])