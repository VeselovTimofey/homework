SELECT user.name, message.text
FROM user, message,
    (SELECT user.id, user.name, MAX(message.date)
    FROM user
    INNER JOIN message
      ON user.id = message.user_id
    GROUP BY user.id) as max_date
WHERE user.id = message.user_id AND user.name = max_date.name AND message.date = max_date.max;