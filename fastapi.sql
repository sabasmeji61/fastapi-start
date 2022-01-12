SELECT name, id AS products_id, is_sale AS on_sale FROM products;
/*SELECT * FROM products*/
/*ORDER BY id ASC*/
SELECT * FROM products WHERE price BETWEEN 50 AND 350;
SELECT * FROM products WHERE price <= 80;

SELECT * FROM products WHERE inventory != 0;
SELECT * FROM products WHERE inventory = 0
ORDER BY name ASC;

SELECT * FROM products WHERE inventory > 0 AND price >= 20;
SELECT * FROM products WHERE price >= 100 OR price < 20
ORDER BY name ASC;

SELECT * FROM products WHERE id IN (1,2,3);
SELECT * FROM products WHERE name LIKE 'TV%';
SELECT * FROM products WHERE name LIKE 'R%';
SELECT * FROM products WHERE name LIKE '%e';
SELECT * FROM products WHERE name NOT LIKE '%e';
SELECT * FROM products WHERE name LIKE '%en%';
SELECT * FROM products WHERE name NOT LIKE '%en%';

SELECT * FROM products WHERE inventory = 0
ORDER BY name ASC;
SELECT * FROM products WHERE inventory = 0
ORDER BY inventory DESC, price DESC;
SELECT * FROM products
ORDER BY price DESC, inventory DESC;
SELECT * FROM products
ORDER BY inventory DESC, price ;

SELECT * FROM products WHERE price > 20 ORDER BY created_at DESC;
SELECT * FROM products  WHERE price > 10 LIMIT 10;
SELECT * FROM products WHERE price > 10 ORDER BY id LIMIT 5 OFFSET 2; /*OFFSET to skip the first 2 rows*/ 


