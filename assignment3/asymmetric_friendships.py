# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 09:24:38 2014

@author: LeBronJames
"""

import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

def reducer(key, list_of_values):
    for i in set(list_of_values):
        if list_of_values.count(i) == 1:
            mr.emit((key, i))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)