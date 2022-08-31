# -*- coding: utf8 -*-
import sys
import os
import os.path
import codecs
from io import open
import cyrtranslit

if __name__ == "__main__":
    lang = sys.argv[1]

    for in_line in sys.stdin:
        print(cyrtranslit.to_cyrillic(in_line.strip(), lang))
