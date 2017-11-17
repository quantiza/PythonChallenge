import urllib
import string

URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'

file_handler = urllib.urlopen(URL)

array_raw = file_handler.readlines()

from_index = array_raw.index('find rare characters in the mess below:\n') + 1

array_valid = array_raw[from_index:]

str_valid = ','.join(array_valid)

answer = filter(lambda x: x in string.letters, str_valid)

print answer