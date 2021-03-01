"""
1. Create an application that asks for an url.

2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. 
Locally means that you should be able to cut your internet connection and still have a functionig html page.

3. When done push all files to you github account. 
(you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).
You will have to use the requests module, the OS module and the subprocesses module for this taks.
"""
import sys, os
import requests
import mimetypes
import subprocess as sp

# check for content-type - works
# if html, create .html file using response.text
# if binary (image, gif) create .(fileextension) using response.content

def main(argv):
    url = input('Enter URL: ')
    token = '9648610bd5c52c29ac49a50fd1a9eeb6ad727fb0' 
    
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    extension = mimetypes.guess_extension(content_type)
    """
    response = requests.head(url)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    
    os.chdir('scrape-exercise')
    
    if 'text/html' in content_type.lower():
        response = download_url(url)
        save_html(response, url)
    else:
        response = download_url(url)
        save_media(response, url, extension)
    
    sp.run(['git', 'config', 'user.email', 'carl_hassel@hotmail.com'])
    sp.run(['git', 'config', 'user.name', 'carlcrede'])
    sp.run(['git', 'pull'])
    sp.run(['git', 'add', '-A'])
    sp.run(['git', 'commit', '-m', 'Downloaded file added'])
    sp.run(['git', 'push', 'https://{}@github.com/carlcrede/scrape-exercise.git'.format(token)])

def download_url(url):
    return requests.get(url, allow_redirects=True)

def save_html(response, url):
    with open('page.html', 'w') as f:
        f.write(response.text)

def save_media(response, url, extension):
    with open('file' + extension, 'wb') as f:
        f.write(response.content)

def getfilename(url):
    return url.rsplit('/', 1)[1]


main(sys.argv)
