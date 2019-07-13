import sys
import os

sys.path.append(os.path.dirname(__file__))
from cssprefixer import process

def do_format(text):
    return process(text)
