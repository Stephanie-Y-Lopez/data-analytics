USE northwind;

-- 1. 
SELECT ProductName, UnitPrice AS MostExpensiveProduct
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- 2.
SELECT products.ProductName, products.UnitPrice AS LeastExpensiveProduct, categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products); 

-- 3.
SELECT orders.OrderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName
FROM orders
JOIN shippers
ON orders.orderID = shippers.ShipperID
WHERE CompanyName = 3;
-- A bit confused still

-- 4.
SELECT OrderID
FROM `order details`
WHERE ProductID = 'Sasquatch Ale';
-- This one is still confusing??

-- 5.
SELECT orders.OrderID, employees.FirstName, employees.LastName
FROM orders
JOIN employees
ON orders.EmployeeID = employees.EmployeeID
WHERE OrderID = 10266;

-- 6.
SELECT orders.OrderID, customers.ContactName AS CustomerName
FROM orders
JOIN customers
ON orders.customerID = customers.CustomerID
WHERE OrderID = 10266;