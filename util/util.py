#!/usr/bin/python
# -*- coding: utf-8 -*-


def execute_cmd(cmd):
    import subprocess as sp

    return sp.check_output(cmd, shell=True).strip()
