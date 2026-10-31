USE northwind;

-- 1. Draft idea
SELECT MIN(UnitPrice) AS cheapestPrice
FROM products;

SELECT Productname, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- 2.
SELECT AVG(UnitPrice) AS AveragePrice
FROM products;

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products;

-- 3. 
SELECT MAX(UnitPrice) AS MostExpensive
FROM products;

SELECT products.ProductName, products.UnitPrice AS ProductPrice, suppliers.CompanyName AS SupplierName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE products.UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- 4.
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM employees;

-- 5. 
SELECT MAX(Salary) AS HighestSalary,
MIN(Salary) AS LowestSalary
FROM employees;

-- 6. 
SELECT suppliers.CompanyName, suppliers.supplierID, COUNT(products.ProductID) AS NumberOfItems
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName, suppliers.SupplierID
ORDER BY suppliers.CompanyName ASC;

-- 7. 
SELECT categories.CategoryName, ROUND(AVG(products.UnitPrice), 2) AS AveragePrice
FROM categories
JOIN products
ON categories.CategoryID = products.CategoryID
GROUP BY Categories.CategoryName;

-- 8. 
SELECT suppliers.CompanyName, COUNT(products.ProductID)
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, suppliers.CompanyName
HAVING COUNT(products.productID) >= 5;

-- 9.
SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;