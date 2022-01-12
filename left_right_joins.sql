/*SELECT posts.*, users.id, email FROM posts LEFT JOIN users ON posts.owner_id = users.id;*/

SELECT * FROM posts RIGHT JOIN users ON posts.owner_id = users.id;