select message, count(1) as total
from (select message, min(create_time) as created_time
      from $channel
      group by user_id, nickname, message
      order by created_time desc) as a
group by message
order by total desc