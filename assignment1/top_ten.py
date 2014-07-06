# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 15:00:22 2014

@author: YunshengWei
"""

import json, sys

def main():
    with open(sys.argv[1]) as tweet_file:
        count = 0
        hashtag_counts = {}
        for line in tweet_file:
            count += 1
            tweet = json.loads(line, encoding = 'utf-8')
            if tweet.has_key(u"entities"):
                for hashtag in tweet[u"entities"][u"hashtags"]:
                    hashtag_counts.setdefault(hashtag[u"text"], 0)
                    hashtag_counts[hashtag[u"text"]] += 1

        hashtag_counts = sorted(hashtag_counts.items(), 
                                key = lambda x : x[1], reverse = True)
        for i in xrange(min(10, count)):
            print hashtag_counts[i][0].encode('utf-8'), hashtag_counts[i][1]
                    
if __name__ == "__main__":
    main()