# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary
FROM Employee 
where salary not in 
(SELECT MAX(salary) as SecondHighestSalary
FROM Employee)
