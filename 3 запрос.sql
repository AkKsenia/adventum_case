/* выявление зависимости числа лайков от промежутка между постами */
select date_diff, round(avg(likes_avg), 2) as avg_likes_amount from 
(select id_, 
date_::date, 
coalesce(lag(date_::date) over (order by date_::date desc), date_::date) as prev_date,
coalesce(lag(date_::date) over (order by date_::date desc), date_::date) - date_::date as date_diff, 
likes_,
coalesce(lag(likes_) over (order by date_::date desc), likes_) as prev_likes,
round((likes_ + coalesce(lag(likes_) over (order by date_::date desc), likes_))::decimal / 2, 1) as likes_avg
from posts_data
order by date_ desc) as table1
where id_ != (select max(id_) from posts_data)
group by date_diff
order by date_diff;
