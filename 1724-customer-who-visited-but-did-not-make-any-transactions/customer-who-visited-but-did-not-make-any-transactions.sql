# Write your MySQL query statement below
SELECT visits.customer_id, count(visits.customer_id) AS count_no_trans
FROM Visits LEFT JOIN Transactions on visits.visit_id = transactions.visit_id
WHERE Transactions.transaction_id is null 
GROUP BY visits.customer_id;