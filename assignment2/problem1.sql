SELECT count(*) FROM(  
  SELECT * FROM frequency
  WHERE docid = '10398_txt_earn');
  
SELECT count(*) FROM(
  SELECT * FROM frequency
  WHERE docid = '10398_txt_earn'
  AND   count = 1);
  
SELECT count(*) FROM(
  SELECT term FROM frequency
  WHERE docid = '10398_txt_earn'
  AND count = 1
  UNION
  SELECT term FROM frequency
  WHERE docid = '925_txt_trade'
  AND count = 1);
  
SELECT count(*) FROM(
  SELECT DISTINCT docid from frequency
  WHERE term = 'parliament');
  
SELECT count(*) FROM(
  SELECT * FROM frequency
  GROUP BY docid
  HAVING SUM(count) > 300
);


SELECT count(*) FROM(
  SELECT DISTINCT a.docid FROM frequency a, frequency b
  WHERE a.docid = b.docid
  AND a.term = 'world'
  AND b.term = 'transactions'
);