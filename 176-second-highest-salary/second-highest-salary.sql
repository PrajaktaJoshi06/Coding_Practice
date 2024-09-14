# Write your MySQL query statement below
SELECT MAX(e1.salary) as SecondHighestSalary
FROM Employee e1 
Join Employee e2
on e1.salary < e2.salary