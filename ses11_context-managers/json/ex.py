import json
import requests

"""
From this api https://api.github.com/orgs/python-elective-fall-2019/repos get 
all names of the repos and write them to a text file.
"""

url = 'https://api.github.com/orgs/python-elective-fall-2019/repos'

response = requests.get(url)

with open('repos.txt', 'w') as f:
    for data in response.json():
        lines = (f'Repo name: {data["name"]}', f'Full repo name: {data["full_name"]}\r\n')
        f.write('\n'.join(lines))



"""
Get all filenames of files ending with .ipynb in the 
code_examples folder in the Lesson-09-context-managers repository.

-- directory doesnt exist..
"""