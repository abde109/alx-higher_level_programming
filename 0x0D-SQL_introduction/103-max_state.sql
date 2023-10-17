-- 103-max_state.sql
-- Max temperature by state, ordered by state name

SELECT state, MAX(temperature) as max_temp 
FROM temperature_table 
GROUP BY state 
ORDER BY state;
