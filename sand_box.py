#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

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

def q9(sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."):
  print sentence
  new_sentence = []
  import random
  for word in sentence.split():
    if len(word) < 5:
      new_word = word
    else:
      l = [a for a in word[1:-1]]
      random.shuffle(l)
      new_word = word[0] + "".join(l) + word[-1]
    new_sentence.append(new_word)
  print " ".join(new_sentence)

def q10(input_file="hightemp.txt"):
  cmd="cat {} | wc -l".format(input_file)
  print execute_cmd(cmd)

def q11():
  # can be sed
  # expand -> expand -t 1 hightemp.txt
  cmd = "cat hightemp.txt | tr '\t' ' ' > ./q11/hightemp_space.txt"
  print execute_cmd(cmd)

def q12():
  for i in range(1, 3):
    cmd = "cat hightemp.txt | cut -f{0} > q12/col{0}.txt".format(i)
    print execute_cmd(cmd)

def q13():
  cmd = "paste q12/col1.txt q12/col2.txt > q13/col1_2.txt"
  print execute_cmd(cmd)

def q14(n=10):
  cmd="head -n{} hightemp.txt".format(n)
  print execute_cmd(cmd)

def q15(n=10):
  cmd="tail -n{} hightemp.txt".format(n)
  print execute_cmd(cmd)

def q16(n=3):
  # q10() -> number of lines in input_file
  input_file = "hightemp.txt"
  cmd="split -l {} {} {}".format(q10(input_file) // n, input_file, "q16/")
  print execute_cmd(cmd)

def q17():
  cmd="cat hightemp.txt | awk '{print $1}' | sort | uniq | wc -l"
  print execute_cmd(cmd)

def q18():
  cmd="sort -r -nk3 {}".format("hightemp.txt")
  print execute_cmd(cmd)

def q19():
  cmd="cut -f1 {} | sort | uniq -c | sort -nk1 -r | cut -f1".format("hightemp.txt")
  print execute_cmd(cmd)

def execute_cmd(cmd):
  import subprocess as sp
  return sp.check_output(cmd, shell=True).strip()

def load_wiki(filename="files/jawiki-country.json"):
  wikis = []
  with open(filename, "r") as fp:
    for line in fp:
      wikis.append(line.strip())
  return wikis

def load_wiki_text():
  wikis = load_wiki()
  lines = []
  for wiki in wikis:
    for line in eval(wiki)['text'].split('\n'):
      lines.append(line)
  return lines

def q20(wikis=load_wiki()):
  for wiki in wikis:
    if "イギリス" == eval(wiki)['title']:
      return eval(wiki)['text']

def q21():
  text = q20()
  lines = []
  for line in text.split('\n'):
    if "Category" in line:
      lines.append(line)
  return lines

def q22():
  lines = q21()
  categories = []
  for line in lines:
    import re
    category = re.search(r'\[\[Category:(.*)\]\]', r'{}'.format(line)).group(1)
    categories.extend([x for x in category.split('|') if x != '*'])
  print ' '.join(categories)

def q23():
  for line in load_wiki_text():
    import re
    r = re.search(r'(^=+ .* =+$)', line)
    if r:
      a = r.group(1).split()
      print "{} {}".format(a[0].count("=") - 1, a[1])

def q24(): # incomplete
  for line in load_wiki_text():
    import re
    # r = re.search(r'<ref>(.*)</ref>', line)
    r = re.search(r'<ref>.*(http://.*.html).*</ref>', line)
    if r:
      print r.group(1)


def q25(): # incomplete
  wikis = load_wiki()
  lines = []
  for wiki in wikis:
    import re
    #r = re.search(r'({{基礎情報.*\n}}\n)', wiki)
    if u'基礎情報' in wiki:
      print '****'
      print wiki
      #print r.group(1)

def q26():
  pass

def q27():
  pass

def q28():
  pass

def q29():
  pass

def load_mecab_txt(filename="files/neko.txt.mecab"):
  with open(filename, 'r') as f:
    return f.readlines()

def q31():
  ret_list = []
  for line in load_mecab_txt():
    a = line.strip().split()
    if len(a) > 1 and '動詞' == a[1].split(',')[0]:
      ret_list.append(a[1])
  return ret_list

def q32():
  for line in q31():
    print line.split(",")[-3]

def q33():
  for line in load_mecab_txt():
    if 'サ変接続' in line and '——' not in line:
      print line.split()[0]

def q34():
  l = []
  for i, line in enumerate(load_mecab_txt()):
    a = line.strip().split()
    if len(a) < 2:
      continue
    l.insert(0, {'word': a[0], 'grammar': a[1].split(',')[0]})
    if len(l) < 3:
      continue
    if '名詞' ==  l[0]['grammar'] and 'の' == l[1]['word'] and '名詞' == l[2]['grammar']:
      print '{}{}{}'.format(l[0]['word'], l[1]['word'], l[2]['word'])
      l = []
      continue
    l.pop()

def q35():
  l = []
  for i, line in enumerate(load_mecab_txt()):
    a = line.strip().split()
    if len(a) < 2:
      continue
    if len(l) % 2 == 0:
      if '名詞' == a[1].split(',')[0]:
        l.insert(0, {'word': a[0], 'grammar': a[1].split(',')[0]})
        continue
    elif len(l) % 2 == 1 and 'の' == a[0]:
      l.insert(0, {'word': a[0], 'grammar': a[1].split(',')[0]})
    else:
      if len(l) > 1:
        for item in l:
          #print item['word'],
          import sys
          sys.stdout.write(item['word'])
        print '\n'
      l = []

def q36():
  d = {}
  for i, line in enumerate(load_mecab_txt()):
    a = line.strip().split()
    if len(a) < 2:
      continue
    if a[0] in d.keys():
      d[a[0]] += 1
    else:
      d[a[0]] = 1
  from operator import itemgetter
  return sorted(d.items(), key=itemgetter(1), reverse=True)

def read_q36_result():
  file="q36/result.txt"
  d = {}
  with open(file, 'r') as fp:
    for line in fp.readlines():
      word, count = line.split()
      d[word] = int(count)
  return d

def q37():
  for i, item in enumerate(q36()):
    if i == 10:
      break
    print '{} {}'.format(item[0], item[1])

# TODO Need to brush up pyplot
def q38():
  import matplotlib.pyplot as plt
  d = read_q36_result()
  tmp_d = {}
  for i in set(d.values()):
    tmp_d[i] = d.values().count(i)
  from operator import itemgetter
  new_d = sorted(tmp_d.items(), key=itemgetter(1), reverse=True)
  plt.figure(figsize=(10, 60))
  plt.barh(range(len(new_d)), [x[1] for x in new_d], align='center')
  plt.yticks(range(len(new_d)), [x[0] for x in new_d])
  plt.savefig('q38/img.png')

def q39():
  pass

class Morph(object):
  def __init__(self, surface, base, pos, pos1):
    self.__surface = surface
    self.__base = base
    self.__pos = pos
    self.__pos1 = pos1

  def output(self):
    print "surface:{}, base:{}, pos:{}, pos1:{}".format(self.__surface, self.__base, self.__pos, self.__pos1)

# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
def q40():
  sentences = []
  with open('files/neko.txt.cabocha.f1', 'r') as fp:
    for i, sentence in enumerate([x for x in fp.read().split('EOS') if r'* 1' in x]):
      import re
      morphs = []
      for words in re.split(r'\* ', sentence):
        for word in words.split('\n'):
          if word.strip() == '' or len(word.split()) == 4:
            continue
          surface = word.split()[0]
          info = word.split()[1].split(',')
          base = info[-3]
          pos = info[0]
          pos1 = info[1]
          if pos1 != '空白':
            morphs.append(Morph(surface, base, pos, pos1))
      sentences.append(morphs)
      if i == 2:
        break
  [x.output() for x in sentences[2]]

def q41():
  pass

if __name__ == '__main__':
  q40()
