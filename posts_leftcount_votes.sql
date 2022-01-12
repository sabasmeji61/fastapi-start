/*SELECT posts.id, COUNT (votes.post_id) FROM posts LEFT JOIN votes ON posts.id = votes.post_id 
GROUP BY posts.id;*/

SELECT posts.*, COUNT (votes.post_id) AS Likes FROM posts LEFT JOIN votes ON posts.id = votes.post_id 
GROUP BY posts.id;
