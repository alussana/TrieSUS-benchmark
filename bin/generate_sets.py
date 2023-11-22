#!/usr/bin/env python3

# Alessandro Lussana <alussana@ebi.ac.uk>

from triesus.random import *
import sys

if __name__ == '__main__':
    
    n_sets = int(sys.argv[1])
    n_items = int(sys.argv[2])
    n_universe = int(sys.argv[3])
    
    sets_dict = random_sets(n_sets,n_items,n_universe)
    
    print_sets(sets_dict)