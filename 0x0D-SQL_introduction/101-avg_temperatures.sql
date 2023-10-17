-- 101-avg_temperatures.sql
-- Calculating average temperature by city, ordered by temperature (descending)

SELECT city, AVG(temperature) as avg_temp 
FROM temperature_table 
GROUP BY city 
ORDER BY avg_temp DESC;
