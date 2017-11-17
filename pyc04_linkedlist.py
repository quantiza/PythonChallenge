import re
import urllib

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

wfile = urllib.urlopen(BASE_URL)

# first = re.findall(r'nothing=\d+', wfile.read())
# num = re.findall(r'\d+', 'nothing=12345')[0]
# wfile.close()
num = '82930'
print('0th : %s' % num)

for i in range(400):
    URL = BASE_URL + '?nothing=' + num
    wfile = urllib.urlopen(URL)
    num = re.findall(r'\d+', wfile.read())[0]
    wfile.close()
    print('%dth : %s' % (i+1, num))

# result : peak.html
