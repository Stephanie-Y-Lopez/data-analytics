/* 
4. 
A) The name of the table that holds NorthWinds items is, Products.
B) The name of the table that holds the categories for NorthWinds items is, Categories.
*/ 
-- 5.
SELECT * FROM employees;
-- Peacock Margaret is the employee with a bird like name.
-- 6. 
SELECT * FROM products;
-- This query returns 77 records and the way to make only 10 records appear max is by right clicking on the employees table and hitting the button 'record limit 1000' and then in the query at the top changing it to 'limit 10 rows'. 
-- Bonus: Im dont think im answering this correctly but there are several different options on how many rows you want select at the top once you are in the query and right clicked 'limit 1000 rows' or by placing the "LIMIT" parameter + the number at the end. 
 -- 7. 
 SELECT * FROM categories; 
-- The ID for the seafood category is 8.ALTER
-- 8. 
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders 
LIMIT 50;