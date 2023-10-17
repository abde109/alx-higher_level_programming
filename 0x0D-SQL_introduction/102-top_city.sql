-- 102-top_city.sql
-- Top 3 cities with highest temperature during July and August

SELECT city, AVG(temperature) as avg_temp 
FROM temperature_table 
WHERE MONTH(date) IN (7, 8) 
GROUP BY city 
ORDER BY avg_temp DESC
LIMIT 3;
