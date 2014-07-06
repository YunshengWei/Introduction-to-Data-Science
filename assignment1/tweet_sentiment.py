# -*- coding: utf-8 -*-

import sys, json

def main():
    with open(sys.argv[1]) as sent_file, \
         open(sys.argv[2]) as tweet_file:
        scores = {}
        for line in sent_file:
            term, score = line.split("\t")
            scores[term.decode('utf-8')] = int(score)
            
        for line in tweet_file:
            tweet = json.loads(line.strip(), encoding = 'utf-8')
            score = sum(scores.get(term, 0) for term in tweet[u"text"].split()) \
            if tweet.has_key(u"text") else 0
            print score
                

if __name__ == '__main__':
    main()
