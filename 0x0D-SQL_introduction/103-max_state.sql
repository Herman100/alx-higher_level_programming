-- Display the maximum temperature for each state, ordered by state name
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
LIMIT 3;
