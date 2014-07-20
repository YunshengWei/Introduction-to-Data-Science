# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 00:49:17 2014

@author: LeBronJames
"""

import MapReduce, sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    order_records = filter(lambda x : x[0] == 'order',
                           list_of_values)
    item_records = filter(lambda x : x[0] == 'line_item',
                          list_of_values)
    for order in order_records:
        for item in item_records:
            mr.emit(order + item)


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)