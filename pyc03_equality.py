import urllib
import os
import re

DATA_NAME = 'pyc_equality_data.txt'

if not os.path.exists(DATA_NAME) or not os.path.getsize(DATA_NAME):
    print DATA_NAME+' is not exist or empty.'
    wfile_handler = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    lfile_handler = open(DATA_NAME, 'w')
    lfile_handler.write(wfile_handler.read())
    wfile_handler.close()
else:
    lfile_handler = open(DATA_NAME, 'r')

# print 'sucessful'
data_raw = lfile_handler.read()        # <type 'str'>
# b = lfile_handler.readlines()   # <type 'list'>
lfile_handler.close()

data_valid = re.split(r'(<!--\n|-->\n)', data_raw)[2]

s = re.split(r'([a-z][A-Z]{3}[a-z][A-Z]{3}[a-z])', data_valid)
ss = re.findall(r'([a-z][A-Z]{3}[a-z][A-Z]{3}[a-z])', data_valid)

def get_parttern(arg):
    m = re.match(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', arg)
    if m:
        return m.group(1)
    else:
        return ''

lst = map(get_parttern, ss)

print ''.join(lst)
# str_content =
