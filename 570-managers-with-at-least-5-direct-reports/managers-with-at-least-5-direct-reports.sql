# Write your MySQL query statement below
Select e2.name
from Employee e1
INNER JOIN employee e2 on e1.managerId = e2.id 
group by e1.managerId having count(e1.id)>=5;