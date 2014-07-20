# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 09:55:58 2014

@author: LeBronJames
"""

import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[:-10], None)

def reducer(key, list_of_values):
    mr.emit(key)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)