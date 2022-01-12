SELECT posts.*, COUNT (votes.post_id) AS Likes FROM posts LEFT JOIN votes ON posts.id = votes.post_id 
WHERE posts.id = 10 GROUP BY posts.id;
