#!/usr/bin/python
# -*- coding: utf-8 -*-


class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.__surface = surface
        self.__base = base
        self.__pos = pos
        self.__pos1 = pos1

    def output(self):
        print("surface:{}, base:{}, pos:{}, pos1:{}".format(
            self.__surface, self.__base, self.__pos, self.__pos1
        ))


# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
def q40():
    sentences = []
    with open("files/neko.txt.cabocha.f1", "r") as fp:
        for i, sentence in enumerate(
            [x for x in fp.read().split("EOS") if r"* 1" in x]
        ):
            import re

            morphs = []
            for words in re.split(r"\* ", sentence):
                for word in words.split("\n"):
                    if word.strip() == "" or len(word.split()) == 4:
                        continue
                    surface = word.split()[0]
                    info = word.split()[1].split(",")
                    base = info[-3]
                    pos = info[0]
                    pos1 = info[1]
                    if pos1 != "空白":
                        morphs.append(Morph(surface, base, pos, pos1))
            sentences.append(morphs)
            if i == 2:
                break
    [x.output() for x in sentences[2]]


def q41():
    pass


if __name__ == "__main__":
    q40()
