/* 
Skills used: 
- Aggregate Functions
- CTEs
- Subqueries
- Converting Data Types
*/
SELECT COUNT(*) FROM RealEstateProject.dbo.Washington;

DELETE FROM RealEstateProject.dbo.Washington WHERE city = 'city';
DELETE FROM RealEstateProject.dbo.Washington WHERE price_per_sqft = 0;

-- Ordering the cities based on the highest price-per-sqft (cities with the hghest price/sqft)
SELECT city, MAX(CAST(price_per_sqft AS FLOAT)) AS max_price_per_sqft
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY max_price_per_sqft DESC;


-- Top 10 cities with the highest average price per sqft
SELECT TOP 10 city, ROUND(AVG(CAST(price_per_sqft AS FLOAT)),2) AS avg_price_per_sqft
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY avg_price_per_sqft DESC;

-- Top 10 maximum HOA cities
SELECT TOP 10 city, MAX(CAST(hoa_fee AS FLOAT)) AS max_hoa
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY max_hoa DESC;

-- Total number of properties for sale in each city, order by the highest number
SELECT TOP 30 city, COUNT(property_id) as count_for_sale_per_city
FROM RealEstateProject.dbo.Washington
GROUP BY city 
ORDER BY count_for_sale_per_city DESC;

-- the most expensive properties (total price, not price-per-sqft)
SELECT TOP 70 city , MAX(CAST(list_price AS FLOAT))AS highest_price
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY highest_price DESC;

-- The least expensive property in each city
SELECT city , MIN(CAST(list_price AS FLOAT))AS lowest_price
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY lowest_price DESC;

-- The lowest price-per-sqft in the 10 most expensive cities
WITH CTE_temp as 
(SELECT TOP 10 city, ROUND(AVG(CAST(price_per_sqft AS FLOAT)),2) AS avg_price_per_sqft
FROM RealEstateProject.dbo.Washington
GROUP BY city
ORDER BY avg_price_per_sqft DESC
)


SELECT wa.city, MIN(CAST(price_per_sqft AS FLOAT)) AS min_price_per_sqft
FROM RealEstateProject.dbo.Washington wa
JOIN CTE_temp
ON CTE_temp.city = wa.city
GROUP BY wa.city
ORDER BY min_price_per_sqft DESC;
