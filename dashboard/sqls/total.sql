select user_id, nickname, message, min(create_time) as created_time
from silphtv
group by user_id, nickname, message
order by created_time desc