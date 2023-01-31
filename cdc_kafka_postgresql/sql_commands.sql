CREATE TABLE recipes (
  recipe_id INT NOT NULL,
  recipe_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (recipe_id),
  UNIQUE (recipe_name)
);

CREATE TABLE ingredients (
  ingredient_id INT NOT NULL, 
  ingredient_name VARCHAR(30) NOT NULL,
  ingredient_price INT NOT NULL,
  PRIMARY KEY (ingredient_id),  
  UNIQUE (ingredient_name)
);

ALTER TABLE ingredients REPLICA IDENTITY FULL;
ALTER TABLE recipes REPLICA IDENTITY FULL;


INSERT INTO recipes (recipe_id, recipe_name) 
VALUES (1,'Tacos'), (2,'Tomato Soup'), (3,'Grilled Cheese');

INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (1, 'Beef', 5),
    (2, 'Lettuce', 1),
    (3, 'Tomatoes', 2);


INSERT INTO recipes (recipe_id, recipe_name) 
VALUES (4,'Pasta'), (5,'Lasagna'), (6,'Fish');

INSERT INTO recipes (recipe_id, recipe_name) 
VALUES (7,'Rice'), (8,'Meat'), (9,'Oats');


INSERT INTO recipes (recipe_id, recipe_name) 
VALUES (10,'Beans'), (11,'Pork'), (12,'Chicken');



INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (1, 'Beef', 5),
    (2, 'Lettuce', 1),
    (3, 'Tomatoes', 2),
    (4, 'Taco Shell', 2),
    (5, 'Cheese', 3),
    (6, 'Milk', 1),
    (7, 'Bread', 2);

INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (4, 'Taco Shell', 2),
    (5, 'Cheese', 3),
    (6, 'Milk', 1);

INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (8, 'Onion', 3);

INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (1, 'Beef', 5),
    (2, 'Lettuce', 1);

INSERT INTO ingredients
    (ingredient_id, ingredient_name, ingredient_price)
VALUES 
    (3, 'Tomatoes', 2),
    (4, 'Taco Shell', 2);