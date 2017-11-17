# chr(65) = 'A'
# ord('a') = 97
# unichr(12345) = u'\u3039'
# ord(u'\u2345') = 9029

# ord

import numpy as np
import string

str_raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def solution_1(str_raw):

    str_valid = ''
    for char in str_raw:
        if 'a' <= char <= 'x':
            char = chr(ord(char) + 2)
        elif 'y' <= char <= 'z':
            char = chr(ord(char) + 2 - 26)
        str_valid += char

    print str_valid


def solution_2(str_raw):
    in_char = 'abcdefghigklmnopqrstuvwxyz'
    out_char = 'cdefghigklmnopqrstuvwxyzab'
    translation = string.maketrans(in_char, out_char)
    str_valid = str_raw.translate(translation)
    print str_valid


solution_2('map')

#
# valid_str = ''
# for x in valid_str_array:
#     valid_str += x
#

