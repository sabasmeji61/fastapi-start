
SELECT users.id, email, COUNT (*) FROM posts LEFT JOIN users ON posts.owner_id = users.id 
GROUP BY users.id;
