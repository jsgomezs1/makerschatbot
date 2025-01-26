-- Eliminación de los datos insertados en inventory.product_type
DELETE FROM inventory.product_type
WHERE "name" IN (
  'Electronics',
  'Clothing',
  'Groceries',
  'Books',
  'Home Appliances',
  'Toys',
  'Beauty Products',
  'Automotive',
  'Health Products',
  'Furniture',
  'Sports Equipment',
  'Pet Supplies',
  'Office Supplies',
  'Jewelry',
  'Musical Instruments',
  'Stationery',
  'Gardening Tools',
  'Kitchenware',
  'Gaming Consoles',
  'Smartphones',
  'Laptops',
  'Cameras',
  'Shoes',
  'Watches',
  'Outdoor Equipment'
);