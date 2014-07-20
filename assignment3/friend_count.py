# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 01:18:17 2014

@author: LeBronJames
"""

import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
    name = record[0]
    mr.emit_intermediate(name, 1)

def reducer(key, list_of_values):
    mr.emit((key, sum(list_of_values)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)