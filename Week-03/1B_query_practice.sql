USE northwind;
SELECT ProductID, ProductName, UnitPrice;
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;

-- 3.
SELECT ProductID, ProductName, UnitPrice, UnitsInStock, Discontinued
FROM products
WHERE Discontinued = 0 AND UnitsInStock >= 1;

-- 4.
SELECT products.ProductID, products.ProductName, categories.CategoryID
FROM Products
JOIN Categories
	ON Products.CategoryID = Categories.CategoryID
WHERE Categories.CategoryName = 'Seafood';

-- 5. 
SELECT products.ProductID, products.ProductName, suppliers.supplierID, suppliers.CompanyName
FROM Products
JOIN suppliers
	ON Products.supplierID = suppliers.supplierID
WHERE suppliers.CompanyName = 'Tokyo Traders';

-- 6. 
SELECT COUNT(*) AS TotalEmployees
FROM Employees;
SELECT FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%Manager%';
