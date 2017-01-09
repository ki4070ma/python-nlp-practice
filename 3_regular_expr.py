#!/usr/bin/python
# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
  q20()
