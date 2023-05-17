-- task 102
SELECT title, SUM(rate) rating
  FROM tv_shows t
       INNER JOIN tv_show_ratings r
       ON t.id = r.show_id
 GROUP BY title
 ORDER BY 2 DESC;
