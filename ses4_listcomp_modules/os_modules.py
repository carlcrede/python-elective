"""
# Do the following task using the os module

1. create a folder and name the folder 'os_exercises.'                                                  
2. In that folder create a file. Name the file 'exercise.py'                                                                            
3. get input from the console and write it to the file.                                                 
4. repeat step 2 and 3 (name the file something else).                                                  
5. read the content of the files and and print it to the console.

"""
import os, sys

# 1. create a folder and name the folder 'os_exercises.
if type(os.listdir('os_exercises')) == None:  
    os.mkdir('os_exercises')

# 2. In that folder create a file. Name the file 'exercise.py'
os.chdir('os_exercises')
open('exercise.py', mode='a+')

# modes:  r is read-only, w is write. a+ is append + read,
# r+ is read + write etc.. 
# 3. get input from the console and write it to the file.
with open('exercise.py', 'a+') as f:
    data = input('Enter text for the file: ')
    f.write(data)

# 4. repeat step 2 and 3 (name the file something else).                                                  
open('anotherFile.txt', 'w')
with open('anotherFile.txt', 'a+') as f:
    data = input('Enter text for .txt file: ')
    f.write(data)

# 5. read the content of the files and and print it to the console.
with open('exercise.py', 'r') as f1:
    with open('anotherFile.txt', 'r') as f2:
        print(f1.read() + f2.read())