select contest_id, 
round(count(distinct r.user_id)*100 / (select count(user_id) from Users),2)  as percentage
from Register r
group by contest_id
order by percentage desc, contest_id asc