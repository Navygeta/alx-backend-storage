-- Creates a trigger that decreases the quantity of an item after adding a new order.
-- The quantity in the table items can be negative.
-- Context: Updating multiple tables for one action from your application can generate issues such as network disconnection, crashes, etc.
-- To maintain data integrity, let MySQL handle it automatically.

CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
