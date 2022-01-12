
SELECT users.id, users.email, COUNT (posts.id) AS userpost_count FROM posts RIGHT JOIN users ON posts.owner_id = users.id 
GROUP BY users.id;
