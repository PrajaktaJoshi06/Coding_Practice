# Write your MySQL query statement below
SELECT  DATE_FORMAT(trans_date, "%Y-%m")as month, country,
COUNT(id) as trans_count, coalesce(SUM(CASE WHEN state = 'approved' then 1 END),0) as approved_count,
SUM(amount) as trans_total_amount, coalesce(SUM(CASE WHEN state = 'approved' then amount END),0) as approved_total_amount
FROM Transactions
Group BY 1,2

#concat(extract(year from trans_date), '-', extract(month from trans_date))