
""" 
Create a commandline tool that checks if the required aguments are present when you run the program, and if not tells you what is missing to run the program.

If you run python python script.py the program should print an error saying Usage: python script.py [-it]{--rm} where the [] means required and the {} means optional. 
"""
import sys
def main(argv):
    if argv[1] != '-it':
        print('Usage: python script.py [-it]{--rm}')
    if len(argv) == 3 and argv[2] != '--rm':
        print('Usage: python script.py [-it]{--rm}')
    elif len(argv) == 3 and argv[2] == '--rm':
        print('Success!')
    else:
        input()

    sys.exit()

main(sys.argv)