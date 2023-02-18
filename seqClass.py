#!/usr/bin/env python

# import libraries
import sys, re
from argparse import ArgumentParser

# input
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = 
"Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# classify the sequence
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()  
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA')
    elif re.search('U', args.seq) and re.search('T', args.seq):
        print ('The sequence is not DNA nor RNA')
    else:
        print ('The sequence can be DNA or RNA')
# adding conditions with "and not" and "and" we can improve the sequence classifier


# find motif in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND!")
    else:
        print("NOT FOUND!")
