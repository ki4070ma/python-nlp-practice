#!/usr/bin/python
# -*- coding: utf-8 -*-

from util.util import execute_cmd


def q10(input_file="hightemp.txt"):
    cmd = "cat {} | wc -l".format(input_file)
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
    cmd = "head -n{} hightemp.txt".format(n)
    print execute_cmd(cmd)


def q15(n=10):
    cmd = "tail -n{} hightemp.txt".format(n)
    print execute_cmd(cmd)


def q16(n=3):
    input_file = "hightemp.txt"
    cmd = "split -l {} {} {}".format(q10(input_file) // n, input_file, "q16/")
    print execute_cmd(cmd)


def q17():
    cmd = "cat hightemp.txt | awk '{print $1}' | sort | uniq | wc -l"
    print execute_cmd(cmd)


def q18():
    cmd = "sort -r -nk3 {}".format("hightemp.txt")
    print execute_cmd(cmd)


def q19():
    cmd = "cut -f1 {} | sort | uniq -c | sort -nk1 -r | cut -f1".format("hightemp.txt")
    print execute_cmd(cmd)


if __name__ == "__main__":
    q10()
