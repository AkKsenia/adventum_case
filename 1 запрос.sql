/* выявление зависимости числа лайков от времени суток публикации */
select
case
when date_::time >= '00:00:00' and date_::time < '06:00:00' then 'ночь'
when date_::time >= '06:00:00' and date_::time < '12:00:00' then 'утро'
when date_::time >= '12:00:00' and date_::time < '18:00:00' then 'день'
else 'вечер'
end as time_of_day, 
round(avg(likes_), 2) as avg_likes_amount 
from posts_data
group by time_of_day;
