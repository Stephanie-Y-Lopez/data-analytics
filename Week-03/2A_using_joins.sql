USE northwind;

-- 1.
SELECT products.productID, products.ProductName, products.UnitPrice, categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY categories.CategoryName ASC, products.ProductName ASC;

-- 2.
SELECT products.productID, products.ProductName, products.UnitPrice, suppliers.ContactName
FROM products
JOIN suppliers
ON products.supplierID = suppliers.supplierID
WHERE products.UnitPrice > 75
ORDER BY products.productName ASC;

-- 3.
SELECT products.productID, products.ProductName, products.UnitPrice, categories.CategoryName, suppliers.ContactName
FROM products
JOIN categories
ON products.categoryID = categories.categoryID
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
ORDER BY products.ProductName ASC; 

-- 4. 
SELECT orders.orderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName AS shippers
FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'Germany'
ORDER BY shippers.CompanyName ASC, orders.ShipName ASC;

-- 5.
SELECT orders.ShipName, orders.ShipAddress, shippers.CompanyName AS shippers,
COUNT(orders.OrderID) AS OrderCount
FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE orders.ShipCountry = 'Germany'
GROUP BY orders.ShipName, orders.ShipAddress, shippers.CompanyName
ORDER BY orders.ShipName ASC; 

-- 6. 
SELECT orders.OrderID, orders.OrderDate, orders.ShipName, orders.ShipAddress
FROM orders
JOIN `order details`
ON orders.OrderID = `order details`.orderID
JOIN products
ON `order details`.ProductID = products.ProductID
WHERE products.ProductName = 'Sasquatch Ale'
ORDER BY orders.orderdate ASC;
