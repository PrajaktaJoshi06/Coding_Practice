-- # Write your MySQL query statement below
-- SELECT MAX(e1.salary) as SecondHighestSalary
-- FROM Employee e1 
-- Join Employee e2
-- on e1.salary < e2.salary

-- SELECT MAX(salary) as SecondHighestSalary
-- FROM Employee 
-- where salary not in 
-- (SELECT MAX(salary) as SecondHighestSalary
-- FROM Employee)

WITH ranked_sal AS (
    SELECT 
        id, 
        salary AS SecondHighestSalary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rank_sal
    FROM Employee
)

SELECT 
    MAX(CASE 
        WHEN rank_sal = 2 THEN SecondHighestSalary 
        ELSE NULL 
    END) AS SecondHighestSalary
FROM ranked_sal;

