# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
From Sales 
NATURAL JOIN Product;