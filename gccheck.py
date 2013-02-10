#-*- coding: utf-8 -*-

import os
import re
import sys
import signal
from requester import requester



quiz_nr = 10
url="http://127.0.0.1/?q=r&n=%i" % quiz_nr
word_list = "words.txt"

stop = False

reqs =requester(url)

def tryIt(test_word):
    try:


        global stop, quiz_nr
        if stop:
            return
        print test_word
        test_word =  test_word.strip()
        test_word = test_word.lower()


        data = {}
        data['no']=str(quiz_nr)
        data['lsg']=test_word
        data['btn_guess']="Pr%FCfen"

        res = reqs.tryData(data)

        # quick and dirty parse response
        gel=  re.search('<font.*>.*</font>',res).group(0)


        print "%s" % (test_word)

        if 'FALSCH' not in gel:
            change=res
            print "found: %s" % gel
            print "try: %s" % test_word
            print "nr :"+quiz_nr

            stop=True


            return


    except Exception as e:
        print e.message




from multiprocessing import Pool

# only 2 request at the same time
p = Pool(processes=2)

def close_pool(signal, frame):

    global stop
    stop=True
    p.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, close_pool)


li = []

for word in open(word_list):
    li.append(word)

p.map(tryIt, li)





