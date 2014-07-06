import sys, json
from collections import defaultdict

def main():
    with open(sys.argv[1]) as sent_file, \
         open(sys.argv[2]) as tweet_file:
        scores = {}
        for line in sent_file:
            term, score = line.split("\t")
            scores[term.decode('utf-8')] = int(score)
        
        nsc_scores = defaultdict(lambda : [0, 0])
        for line in tweet_file:
            tweet = json.loads(line.strip(), encoding = 'utf-8')
            if not tweet.has_key(u"text"):
                score = 0
                continue
            score = sum(scores.get(term, 0) for term in tweet[u"text"].split())
            for term in tweet[u"text"].split():
                if not scores.has_key(term):
                    nsc_scores[term][0] += score
                    nsc_scores[term][1] += 1
            
        for term, (total_score, count) in nsc_scores.iteritems():
            print term.encode('utf-8'), total_score / float(count)

if __name__ == '__main__':
    main()
