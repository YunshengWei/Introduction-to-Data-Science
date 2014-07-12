SELECT SUM(a.count * b.count) 
FROM frequency a, frequency b
WHERE a.docid = '10080_txt_crude'
AND b.docid = '17035_txt_earn'
AND a.term = b.term;


SELECT b.docid, SUM(a.count * b.count) as similarity
FROM
(SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) as a,
frequency as b
WHERE  a.term = b.term
GROUP BY b.docid
ORDER BY similarity DESC;