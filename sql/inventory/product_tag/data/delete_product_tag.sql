-- Eliminación de datos en inventory.product_tag basados en product_id y tag_id
DELETE FROM inventory.product_tag
WHERE (product_id, tag_id) IN (
  ('1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '79030460-246d-47c2-8a7b-f136d110a4d8'), -- Coca-Cola Vending Machine - New Arrival
  ('1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '22ae3361-7354-4e4d-a63c-382bff229a3c'), -- Coca-Cola Vending Machine - Best Seller
  ('bae811a4-4bc1-4380-909b-c9e145bf03ba', '7776a9a5-fd15-4c98-b996-6fe96ad3aafa'), -- Sprite Cooling Dispenser - Discount
  ('bae811a4-4bc1-4380-909b-c9e145bf03ba', '2c44456f-2bc5-4bd5-8093-5372e589ec10'), -- Sprite Cooling Dispenser - Eco-Friendly
  ('1e41619a-64bb-4474-a83f-eecb66aa9a89', '1303b429-d2e5-4366-9e61-5af4ec138d28'), -- Pepsi Cooler - Popular
  ('1e41619a-64bb-4474-a83f-eecb66aa9a89', '9cb8e914-f21c-4d4e-9db6-335d7a4a284b'), -- Pepsi Cooler - Trending
  ('eab0933f-7929-485b-b8f7-499ddde9384c', '0d415ecf-ed7c-450d-b3b4-7cd3a845f251'), -- GE Washing Machine - Energy Efficient
  ('eab0933f-7929-485b-b8f7-499ddde9384c', '62df38ff-fe19-4e0c-91a6-0fe55e6b2c25'), -- GE Washing Machine - Luxury
  ('c563ed80-6c73-46be-aa2e-9dd81110b7c9', '7543d7b5-4392-49b9-81f0-9342f8591b08'), -- PlayStation 5 - Refurbished
  ('c563ed80-6c73-46be-aa2e-9dd81110b7c9', '22ae3361-7354-4e4d-a63c-382bff229a3c'), -- PlayStation 5 - Best Seller
  ('3e826991-60d7-48c4-9331-a17b3511b176', '540f264a-d75b-4457-8736-1ebcd1362cff'), -- Nike Air Max 97 - Family-Friendly
  ('3e826991-60d7-48c4-9331-a17b3511b176', 'c74fbead-0d32-46c6-a013-20cd98e136b7'), -- Nike Air Max 97 - Seasonal
  ('8dbef708-8626-4535-a497-6b67d06b32ab', '1d3fc02d-b509-486e-a78d-723536f531e4'), -- Adidas Ultraboost 21 - Outdoor Use
  ('8dbef708-8626-4535-a497-6b67d06b32ab', 'bebaf501-bc66-46cb-b372-9836ff6981a5')  -- Adidas Ultraboost 21 - Portable
);