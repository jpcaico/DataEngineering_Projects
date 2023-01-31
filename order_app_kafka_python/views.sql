CREATE VIEW `orders_dataset.top_products_per_country` AS (
SELECT country_name, item_id, COUNT(item_id) as frequency
FROM `orders_dataset.orders_table`
GROUP BY country_name, item_id
ORDER BY frequency DESC
);

CREATE VIEW `orders_dataset.most_revenue` AS (
SELECT item_id, SUM(item_price) as total_price
FROM `orders_dataset.orders_table`
GROUP BY item_id
ORDER BY SUM(item_price) DESC
);