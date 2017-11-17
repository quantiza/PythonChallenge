import urllib
import os
import pickle

DATA_NAME = 'pyc_peak_data.txt'

if not os.path.exists(DATA_NAME) or not os.path.getsize(DATA_NAME):
    print DATA_NAME+' is not exist or empty.'
    wfile_handler = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    lfile_handler = open(DATA_NAME, 'w')
    lfile_handler.write(wfile_handler.read())
    wfile_handler.close()
    lfile_handler.close()
else:
    lfile_handler = open(DATA_NAME, 'r')

data = pickle.load(lfile_handler)

for item in data:
    s = ''.join([i[1]*i[0] for i in item])
    print s
