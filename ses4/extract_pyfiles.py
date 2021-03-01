import sys, os
import subprocess as sp
import shutil
from zipfile import ZipFile

def main(argv):
    # check input
    check_input(argv)

    # change dir and get files
    files = os.listdir(argv[1])

    # get all .py files
    pyfiles = [ f for f in files if os.path.splitext(f)[1] == '.py' ]
    
    # create temp dir
    os.mkdir(argv[3])

    # add .py files to temp dir
    # subprocess couldnt find file, using shutil instead. (was not using Docker..)
    for f in pyfiles:
        shutil.copy2(f, argv[3])

    # put all .py files into new .zip folder
    if len(argv) > 4 and argv[4] == '--zip':
        with ZipFile(argv[3] + '/' + argv[5], 'w') as zf:
            for f in pyfiles:
                zf.write(f)

def check_input(argv):
    if len(argv) < 2:
        print('Usage: python script.py [dir][--todir]{--zip}')
        sys.exit()
    if len(argv) == 3 and argv[2] != '--todir':
        print('Usage: python script.py [dir][--todir]{--zip}')
        sys.exit()

main(sys.argv)