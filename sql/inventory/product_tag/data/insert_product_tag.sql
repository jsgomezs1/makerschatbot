-- Inserción de datos en la tabla inventory.product_tag
INSERT INTO inventory.product_tag (id, product_id, tag_id)
VALUES
  -- Coca-Cola Vending Machine
  (gen_random_uuid(), '1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '79030460-246d-47c2-8a7b-f136d110a4d8'), -- New Arrival
  (gen_random_uuid(), '1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '22ae3361-7354-4e4d-a63c-382bff229a3c'), -- Best Seller

  -- Sprite Cooling Dispenser
  (gen_random_uuid(), 'bae811a4-4bc1-4380-909b-c9e145bf03ba', '7776a9a5-fd15-4c98-b996-6fe96ad3aafa'), -- Discount
  (gen_random_uuid(), 'bae811a4-4bc1-4380-909b-c9e145bf03ba', '2c44456f-2bc5-4bd5-8093-5372e589ec10'), -- Eco-Friendly

  -- Pepsi Cooler
  (gen_random_uuid(), '1e41619a-64bb-4474-a83f-eecb66aa9a89', '1303b429-d2e5-4366-9e61-5af4ec138d28'), -- Popular
  (gen_random_uuid(), '1e41619a-64bb-4474-a83f-eecb66aa9a89', '9cb8e914-f21c-4d4e-9db6-335d7a4a284b'), -- Trending

  -- GE Washing Machine
  (gen_random_uuid(), 'eab0933f-7929-485b-b8f7-499ddde9384c', '0d415ecf-ed7c-450d-b3b4-7cd3a845f251'), -- Energy Efficient
  (gen_random_uuid(), 'eab0933f-7929-485b-b8f7-499ddde9384c', '62df38ff-fe19-4e0c-91a6-0fe55e6b2c25'), -- Luxury

  -- PlayStation 5
  (gen_random_uuid(), 'c563ed80-6c73-46be-aa2e-9dd81110b7c9', '7543d7b5-4392-49b9-81f0-9342f8591b08'), -- Refurbished
  (gen_random_uuid(), 'c563ed80-6c73-46be-aa2e-9dd81110b7c9', '22ae3361-7354-4e4d-a63c-382bff229a3c'), -- Best Seller

  -- Nike Air Max 97
  (gen_random_uuid(), '3e826991-60d7-48c4-9331-a17b3511b176', '540f264a-d75b-4457-8736-1ebcd1362cff'), -- Family-Friendly
  (gen_random_uuid(), '3e826991-60d7-48c4-9331-a17b3511b176', 'c74fbead-0d32-46c6-a013-20cd98e136b7'), -- Seasonal

  -- Adidas Ultraboost 21
  (gen_random_uuid(), '8dbef708-8626-4535-a497-6b67d06b32ab', '1d3fc02d-b509-486e-a78d-723536f531e4'), -- Outdoor Use
  (gen_random_uuid(), '8dbef708-8626-4535-a497-6b67d06b32ab', 'bebaf501-bc66-46cb-b372-9836ff6981a5'); -- Portable