import urllib.request
from urllib.request import urlretrieve
import requests
import os

def cbk(a,b,c):
    '''''Callback function
    @a:Downloaded data block
    @b:Block size
    @c:Size of the remote file
    '''
    per=a*b/c
    if per>1.0:
        per=1.0
    # print("%.2f%%" % (per,))
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(per * 50), per * 100), end="", flush=True)


def get_from_surfdrive(url, destination):

    if url.endswith('download'):
        URL = url
    else:
        URL = '/'.join((url, 'download'))

    if URL:
        urlretrieve(URL, destination, cbk)
    print("")


def get_from_googledrive(url, lpath, lname):
    get_from_googledrive_slient(url, lpath, lname)

def get_from_googledrive_slient(url, lpath, lname):
    id0 = url.find('/d/')
    id1 = url.find('/view')

    id = url[id0 + 3: id1]

    URL = 'https://docs.google.com/uc?export=download'

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)

    token = get_confirm_google_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    destination = os.path.join(lpath, lname)
    CHUNK_SIZE = 32768
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def get_confirm_google_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
        else:
            print('False link! Please copy the right link.')
            raise Exception