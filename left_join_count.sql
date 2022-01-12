
SELECT users.id, users.email, COUNT (posts.id) AS userpost_count FROM posts LEFT JOIN users ON posts.owner_id = users.id 
GROUP BY users.id;
