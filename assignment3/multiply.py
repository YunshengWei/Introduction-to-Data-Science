# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 09:59:35 2014

@author: LeBronJames
"""

import MapReduce, sys
from collections import defaultdict

mr = MapReduce.MapReduce()

appeared = set()
def mapper(record):
    row_a = 5
    col_b = 5
    if record[0] == 'a':
        for i in xrange(col_b):
            mr.emit_intermediate((record[1], i), record)
    if record[0] == 'b':
        for i in xrange(row_a):
            mr.emit_intermediate((i, record[2]), record)

def reducer(key, list_of_values):
    i, j = key[0], key[1]
    a = filter(lambda x : x[0] == 'a', list_of_values)
    a = defaultdict(int, {x[2] : x[3]
                    for x in a})
    b = filter(lambda x : x[0] == 'b', list_of_values)
    b = defaultdict(int, {x[1] : x[3]
                    for x in b})
    value = sum([a[x] * b[x] for x in a])
    mr.emit((i, j, value))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)