# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 12:05:36 2014

@author: YunshengWei
"""

import sys, json
from collections import defaultdict

def main():
    with open(sys.argv[1]) as tweet_file:
        count = defaultdict(int)
        for line in tweet_file:
            tweet = json.loads(line, encoding = 'utf-8')
            if tweet.has_key(u"text"):
                for term in tweet[u"text"].split():
                    count[term] += 1
        
        total_count = float(sum(c for c in count.itervalues()))
        for term, c in count.iteritems():
            print term.encode('utf-8'), c / total_count

if __name__ == "__main__":
    main()