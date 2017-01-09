#!/usr/bin/python
# -*- coding: utf-8 -*-


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

if __name__ == '__main__':
  q31()
