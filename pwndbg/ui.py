#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A few helpers for making things print pretty-like.
"""
from __future__ import print_function
from __future__ import unicode_literals

import fcntl
import struct
import sys
import termios

import pwndbg.arch
import pwndbg.color

def get_term_size():
    try:
        height, width = struct.unpack('hh', fcntl.ioctl(sys.stdin.fileno(), termios.TIOCGWINSZ, '1234'))
    except:
        height = 60
        width = 80
    return (height, width)

def banner(title):
    title = title.capitalize()
    _height, width = get_term_size()

    skip = 3
    fill_char = u'─'
    margin = 1

    before = fill_char * skip
    before = pwndbg.color.bold(pwndbg.color.cyan(before))

    middle = pwndbg.color.bold(pwndbg.color.yellow(title))

    after_length = width - len(title) - skip - 2 * margin
    after = fill_char * after_length
    after = pwndbg.color.bold(pwndbg.color.cyan(after))

    return ''.join([before, ' ' * margin, middle, ' ' * margin, after])

def addrsz(address):
    address = int(address) & pwndbg.arch.ptrmask
    return "%{}x".format(2*pwndbg.arch.ptrsize) % address
