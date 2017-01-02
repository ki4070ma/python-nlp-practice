#!/usr/bin/python
# -*- coding: utf-8 -*-

def q0():
  print 'stressed'[::-1]

def q1():
    print u'パタトクカシーー'[0:8:2]

def q2():
    a=u'パトカー'
    b=u'タクシー'
    print ''.join([a[x] + b[x] for x in range(len(a))])

def q3():
    a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print [len(x.replace('.', '').replace(',', '')) for x in a.split()]

def q4():
    l="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    ret_dict = {}
    for i, a in enumerate(l.split()):
        if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
            ret_dict[a[0]] = i+1
        else:
            ret_dict[a[:2]] = i+1
    print ret_dict

def q5(n=2, str="I am an NLPer"):
    print "****word"
    words = str.split()
    for i, a in enumerate(words):
        if i == len(words) - n + 1:
            break
        print ' '.join([words[j] for j in range(i, i+n)])

    print "*****character"
    print ngram_char(n, str)

def ngram_char(n=2, str="I am an NLPer"):
    ret_list = []
    length = len(str)
    for i in range(length):
        if i == length - n + 1:
            break
        ret_list.append(''.join([str[j] for j in range(i, i+n)]))
    return ret_list

def q6():
    X=set(ngram_char(2, "paraparaparadise"))
    print X
    Y=set(ngram_char(2, "paragraph"))
    print Y

    print "****plus"
    print (X | Y)

    print "****times"
    print (X & Y)

    print "****minus"
    print (X ^ Y)

def q7(x=12, y="気温", z=22.4):
    print "{}時の{}は{}".format(x, y, z)

def q8(sentence="Hello, my name is Atsushi. Age is 31."):
    ret = ""
    for i in range(len(sentence)):
        if sentence[i].islower():
            ret += str(ord(sentence[i]))
        else:
            ret += sentence[i]
    print ret

def q8_decode(sentence="H101108108111, 109121 11097109101 105115 A116115117115104105. A103101 105115 31."):
    for c in range(len(sentence)):
        
    print sentence

if __name__ == '__main__':
    q8()
