INSERT INTO products (name, price, inventory) VALUES('Tortilla', 4, 1000);

INSERT INTO products (price, name, inventory) VALUES(10000, 'car', 1000) RETURNING *;
INSERT INTO products (price, name, inventory) VALUES(10000, 'car', 1000) RETURNING name;
SELECT * FROM products;

INSERT INTO products (price, name, inventory) VALUES (50, 'Laptop', 25), (60, 'Monitor', 4) RETURNING *;
INSERT INTO products (price, name, inventory) VALUES (50, 'Laptop', 25), (60, 'Monitor', 4) 
RETURNING id, created_at, name;

DELETE FROM products WHERE id = 10;
DELETE FROM products WHERE id = 11 RETURNING *;

DELETE FROM products WHERE inventory = 0 RETURNING *;
SELECT * FROM products;

UPDATE products SET name = 'Flour tortilla', price = 40 WHERE id = 17;
UPDATE products SET is_sale = true WHERE id = 16 RETURNING *; 
UPDATE products SET is_sale = true WHERE id > 15 RETURNING *; 

