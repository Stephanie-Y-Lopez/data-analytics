USE northwind;
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;

SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 3.
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 4.
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;

-- 5.
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- 6. 
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25 
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- 7.
SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title
ORDER BY Title ASC;

-- 8.
SELECT EmployeeID, FirstName, LastName, Salary
FROM employees
WHERE Salary < 2500 
AND Salary >= 2000
ORDER BY Salary DESC;
