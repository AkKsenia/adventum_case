/* выявление зависимости числа лайков от дня недели публикации */
select 
case
when date_part('isodow', date_) = 1 then 'Mon'
when date_part('isodow', date_) = 2 then 'Tue'
when date_part('isodow', date_) = 3 then 'Wed'
when date_part('isodow', date_) = 4 then 'Thu'
when date_part('isodow', date_) = 5 then 'Fri'
when date_part('isodow', date_) = 6 then 'Sat'
else 'Sun'
end as day_of_week, 
round(avg(likes_), 2) as avg_likes_amount 
from posts_data
group by date_part('isodow', date_)
order by date_part('isodow', date_);
