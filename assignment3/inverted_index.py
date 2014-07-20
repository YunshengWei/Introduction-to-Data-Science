# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 00:40:54 2014

@author: LeBronJames
"""

import sys, MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    document_id = record[0]
    text = record[1]
    words = set(text.split())
    for word in words:
      mr.emit_intermediate(word, document_id)

def reducer(key, list_of_values):
    mr.emit((key, list_of_values))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)