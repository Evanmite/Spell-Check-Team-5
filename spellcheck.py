import numpy as np
import pandas as pd
import re # Regular Expressions
from collections import Counter
import string
import enchant

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        words = []
        
        for line in text:
            words = words + re.findall(r'\w+', line.lower()) # RE for making a words list from file
    return words

def split(word):
    return[(word[:i], word[i:]) for i in range(len(word) + 1)] #

def delete(word):
    return [l + r[1:] for l,r in split(word) if r] # l,r left, right for above

def swap(word):
    return [l + r[1] + r[0] + r[2:] for l,r in split(word) if len(r)>1]
