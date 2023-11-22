#!/usr/bin/env python3

# from <https://stackoverflow.com/questions/48459376/>

from itertools import chain, combinations as comb
import re

def ProcessSet(l):
    """Turn a line [read from text file] into a tuple of (label, values)."""
    label = l[l.find(':')-1]
    vals = re.compile('{(.+)}').findall(l.rstrip())[0].split(',')
    return label, vals

def GetSubsets(s):
    """
    Get all subsets of a given set (including the empty set).
    """
    return list(chain(*map(lambda x: comb(s, x), range(0, len(s)))))

def GetPowerset(s):
    """
    Get the powerset of a given set (all subsets incl. empty and full set).
    """
    return list(chain(*map(lambda x: comb(s, x), range(0, len(s)+1))))

# read the text lines into a list
with open("misc/50_50_50.txt", "r") as f:
    sets = [ProcessSet(l) for l in f.readlines()]

all_subsets = [GetSubsets(s[1]) for s in sets]
powersets  = [GetPowerset(s[1]) for s in sets]

for i in range(0, len(sets)):
    # declare label (l) and subsets (ss) for current loop iteration
    l, ss = sets[i][0], all_subsets[i]
    # list the other powersets to compare against
    ops = [x for ind, x in enumerate(powersets) if ind != i]
    # find unique subsets: those that are only a subset of the current set
    # and not found in the powerset of any of the other sets
    uss = list(set(ss)-set([x for y in ops for x in y if x in ss]))
    #uss = []
    #for s in ss:
    #    contains_s = [(s in ps) for ps in ops]
    #    if not any(contains_s):
    #        uss.append(s)
    str_uss = ', '.join([f"({', '.join(x)})" for x in uss])
    print(f"set {l}: {str_uss}")