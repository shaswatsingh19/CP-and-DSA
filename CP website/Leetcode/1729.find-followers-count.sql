# https://leetcode.com/problems/find-followers-count/
select user_id,count(DISTINCT follower_id) as followers_count
from followers
group by user_id
order by user_id