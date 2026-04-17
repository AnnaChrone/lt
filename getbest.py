#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    num_col = None #FIX: starts index from 0
    mark_col = None

    for i,head in enumerate(headings): #FIX: allows for correct indexing
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = None
    best_idx = None
    for line in f:
        data = line.strip().split(",")
        if len(data) <= max(num_col, mark_col):
            continue

        mark = int(data[mark_col])
        if best is None or mark > best:
            best = mark
            best_idx = data[num_col] #FIX: best_idx was not being updated
    return best_idx, best

f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))
