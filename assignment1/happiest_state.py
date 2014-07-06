# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 12:52:41 2014

@author: YunshengWei
"""

import sys, json
from collections import defaultdict
import states

def main():
    with open(sys.argv[1]) as sent_file, \
         open(sys.argv[2]) as tweet_file:
        scores = {}
        for line in sent_file:
            term, score = line.split("\t")
            scores[term.decode('utf-8')] = int(score)
            
        state_scores = defaultdict(lambda : [0, 0])
        for line in tweet_file:
            tweet = json.loads(line.strip(), encoding = 'utf-8')
            score = sum(scores.get(term, 0) for term in tweet[u"text"].split()) \
            if tweet.has_key(u"text") else 0
            if tweet.has_key(u"user"):
                if tweet[u"user"].has_key(u"location"):
                    locations = tweet[u"user"][u"location"].upper().split(',')
                    for location in locations:
                        if states.states.has_key(location):
                            state_scores[location][0] += score
                            state_scores[location][1] += 1
        
        print sorted(state_scores.items(), key = lambda x : x[1][0] / float(x[1][1]))[-1][0]

if __name__ == '__main__':
    main()