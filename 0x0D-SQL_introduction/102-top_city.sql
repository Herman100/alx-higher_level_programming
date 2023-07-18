-- Display the top 3 cities with the highest average temperature during July and August, ordered by temperature (descending)
SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
