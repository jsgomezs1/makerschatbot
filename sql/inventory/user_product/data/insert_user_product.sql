-- Versión corregida del INSERT (UTF-8 sin caracteres especiales)
INSERT INTO inventory.user_product (id, price, recommendation_rating, product_id, user_id)
VALUES
  -- Usuario: Reid Hoffman
  (gen_random_uuid(), 2500.00, 4.8, '1dbe5de5-17de-4538-95c1-e6e2d2b73b79', '6e194a56-12c7-4dd2-8037-70ec8f02c53a'), -- Coca-Cola Vending Machine
  (gen_random_uuid(), 199.99, 4.5, 'bae811a4-4bc1-4380-909b-c9e145bf03ba', '6e194a56-12c7-4dd2-8037-70ec8f02c53a'), -- Sprite Cooling Dispenser

  -- Usuario: Paul Graham
  (gen_random_uuid(), 500.00, 4.9, '1e41619a-64bb-4474-a83f-eecb66aa9a89', 'cbf40c64-ddf6-49dc-a27f-f89a042a1a7b'), -- Pepsi Cooler
  (gen_random_uuid(), 1200.00, 4.7, 'eab0933f-7929-485b-b8f7-499ddde9384c', 'cbf40c64-ddf6-49dc-a27f-f89a042a1a7b'), -- GE Washing Machine

  -- Usuario: Emmett Shear
  (gen_random_uuid(), 1800.00, 4.6, '164cf7fe-cfb1-4b63-a074-3ac3cc5f76c6', '0efb809c-df0a-45e2-a898-fe07e63983a7'), -- Samsung Smart Refrigerator
  (gen_random_uuid(), 400.00, 4.3, 'c563ed80-6c73-46be-aa2e-9dd81110b7c9', '0efb809c-df0a-45e2-a898-fe07e63983a7'), -- PlayStation 5

  -- Usuario: Sara Blakely
  (gen_random_uuid(), 1500.00, 4.8, 'a7f3b1e5-c25f-45f9-b01e-9fc48f580124', 'd1e8303f-4a87-4548-97cb-615b806d1ce5'), -- Alienware Aurora R14
  (gen_random_uuid(), 999.99, 4.7, '137636b5-be42-4040-b70a-fc39a3fdc247', 'd1e8303f-4a87-4548-97cb-615b806d1ce5'), -- Dell XPS 13

  -- Usuario: Whitney Wolfe Herd
  (gen_random_uuid(), 109.99, 4.4, '3e826991-60d7-48c4-9331-a17b3511b176', 'f7521d87-c7ae-45e6-b167-2164116d1390'), -- Nike Air Max 97
  (gen_random_uuid(), 120.00, 4.5, '8dbef708-8626-4535-a497-6b67d06b32ab', 'f7521d87-c7ae-45e6-b167-2164116d1390'); -- Adidas Ultraboost 21