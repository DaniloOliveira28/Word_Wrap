#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import getopt

from word_wrap import *


def usage():
    print "Usage: main.py -l [1-inf]"
    print "-l : número máximo de colunas"


def main(argv):
    textFile = open("./Data/in.txt", "r")
    text = textFile.read()
    textFile.close()
    length = None

    try:
        opts, args = getopt.getopt(argv, "hl:")
    except getopt.GetoptError:
        print "main.py -l [1-inf]"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit(0)
        elif opt in ("-l"):
            length = int(arg)

    if length is None:
        usage()
        exit()

    text = text.split("\n")

    for line in text:
        line = line.split(" ")
        wordwrap_dp(line, length)


if __name__ == "__main__":
    main(sys.argv[1:])
