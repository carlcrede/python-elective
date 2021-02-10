"""
1. Create a file and call it lyrics.txt (it does not need to have any content)

2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.

3. open and read the content and write it to your terminal window. 
* you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).
"""

# 1
# First argument is name of file, second is what kind of operation we want to do
# w means we want to write to file, file will be created if it doesnt exist, + indicates both read and write operations
f = open('lyrics.txt', 'w+')
print(f'Name of file: {f.name}')

# 2
f = open('songs.docx', 'w+')
for i in range(3):
    f.write(f'This is line number {i+1}\n')

# 3
f = open('songs.docx')
print(f'Reading file with read():\r\n\n{f.read()}')

f = open('songs.docx')
print(f'Reading file with readline():\r\n\n{f.readline()}')

f = open('songs.docx')
print(f'Reading file with readlines():\r\n\n{f.readlines()}')