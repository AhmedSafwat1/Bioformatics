import re
import string
import uuid
import random
import base64
import sys,md5
import math
import Tkinter
'''
 first function in books 2.7
 count the word in the file
 using regular expression
 + one or more
'''
def count_word(path):
    total = 0
    line = []
    line_reduce = [0]
    file = open(path, "r")
    for i in file:
        line = re.split(r'[ \n]+', i);
        line_reduce = [var for var in line if var != '']
        print line_reduce
        total = total + len(line_reduce)
    print total
    return total;



'''the secnd programing count the freq of word in file'''
def count_frq(path):
    word_list = []
    freq_list = []
    freq = {}
    in_text = open(path, "r")
    in_text_string = in_text.read()
    out_text = open("output.txt", "w")
    in_text_string = string.lower(in_text_string)
    word_list = re.findall(r'(\b[a-z]{3,15}\b)', in_text_string)
    for item in word_list:
        count = freq.get(item, 0)
        freq[item] = count + 1
    freq_list = freq.keys()
    sort_list = sorted(freq_list)
    for i in sort_list:
        print>> out_text, i, freq[i]
    return freq

'''
 the third program for encrption and decrption

'''
def Enc_dec(path):
    sample_file = open(path, "rb")
    string = sample_file.read()
    sample_file.close()
    print base64.encodestring(string)
    print base64.decodestring(base64.encodestring(string))

'''
   cut the phares
'''

def cut_title():
    all_text = "I am here. you are here. We are all here.";
    sentence_list = re.split(r'[\.\!\?] +(?=[A-Z])', all_text)
    print "\n".join(sentence_list)



'''
 get the usrer name and convert to hex

'''
def red_conv():
    print "What is your full name?"
    line = sys.stdin.readline()
    line = line.rstrip()
    md5_object = md5.new()
    md5_object.update(line)
    print md5_object.hexdigest()



'''
red the image and convert to encode
'''
def encodimg(imagpath):
    import md5
    import string
    md5_object = md5.new()
    sample_file = open(imagpath, "rb")
    string = sample_file.read()
    sample_file.close()
    md5_object.update(string)
    md5_string = md5_object.digest()
    print "".join(["%02X " % ord(x) for x in md5_string]).strip()



'''
   prime number
'''

def prime_from_toEnd(start,end):
    for i in range(start, end):
        upper = math.sqrt(i)
        upper = int(upper)
        for thing in range(2, upper):
            state = 1
            if (i % thing == 0):
                state = 0
                break
        if (state == 1):
                print i,