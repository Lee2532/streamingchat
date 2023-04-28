select nickname, count(1) as total
from (select nickname
      from $channel
      group by user_id, nickname, message) as A
group by nickname
order by total desc;
