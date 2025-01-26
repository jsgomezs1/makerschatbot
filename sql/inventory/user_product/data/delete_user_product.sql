-- Eliminación de datos en inventory.user_product basados en product_id y user_id
DELETE FROM inventory.user_product
WHERE (product_id, user_id) IN (
  ('1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '6e194a56-12c7-4dd2-8037-70ec8f02c53a'), -- Coca-Cola Vending Machine - Reid Hoffman
  ('bae811a4-4bc1-4380-909b-c9e145bf03ba', '6e194a56-12c7-4dd2-8037-70ec8f02c53a'), -- Sprite Cooling Dispenser - Reid Hoffman
  ('1e41619a-64bb-4474-a83f-eecb66aa9a89', 'cbf40c64-ddf6-49dc-a27f-f89a042a1a7b'), -- Pepsi Cooler - Paul Graham
  ('eab0933f-7929-485b-b8f7-499ddde9384c', 'cbf40c64-ddf6-49dc-a27f-f89a042a1a7b'), -- GE Washing Machine - Paul Graham
  ('164cf7fe-cfb1-4b63-a074-3ac3cc5f76c6', '0efb809c-df0a-45e2-a898-fe07e63983a7'), -- Samsung Smart Refrigerator - Emmett Shear
  ('c563ed80-6c73-46be-aa2e-9dd81110b7c9', '0efb809c-df0a-45e2-a898-fe07e63983a7'), -- PlayStation 5 - Emmett Shear
  ('a7f3b1e5-c25f-45f9-b01e-9fc48f580124', 'd1e8303f-4a87-4548-97cb-615b806d1ce5'), -- Alienware Aurora R14 Gaming Desktop - Sara Blakely
  ('137636b5-be42-4040-b70a-fc39a3fdc247', 'd1e8303f-4a87-4548-97cb-615b806d1ce5'), -- Dell XPS 13 - Sara Blakely
  ('3e826991-60d7-48c4-9331-a17b3511b176', 'f7521d87-c7ae-45e6-b167-2164116d1390'), -- Nike Air Max 97 - Whitney Wolfe Herd
  ('8dbef708-8626-4535-a497-6b67d06b32ab', 'f7521d87-c7ae-45e6-b167-2164116d1390')  -- Adidas Ultraboost 21 - Whitney Wolfe Herd
);