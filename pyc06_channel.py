import os
import re

# file numbers in channel
BASE_DIR = 'channel/'

file_amount = len(os.listdir(os.path.dirname(BASE_DIR)))

file_name = '90052'

for i in range(file_amount):
    lfile = open(BASE_DIR + file_name + '.txt', 'r')
    file_name = re.findall(r'\d+', lfile.read())[0]
    lfile.close()
    print i, file_name