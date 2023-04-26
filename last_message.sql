SELECT message.text
FROM message
WHERE message.data IN
	(SELECT MAX(message.data)
	FROM user
	INNER JOIN message
  	  ON user.id = message.user_id
	GROUP BY user.id);