-- Versión corregida del INSERT (UTF-8 sin caracteres especiales)
INSERT INTO inventory.user_product (id, price, recommendation_rating, product_id, user_id)
VALUES
  -- Usuario: Reid Hoffman (user_id: a26)
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380ab9', 2500.00, 4.8, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a81', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a26'), -- Coca-Cola Vending Machine
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380aba', 199.99, 4.5, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a82', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a26'), -- Sprite Cooling Dispenser

  -- Usuario: Paul Graham (user_id: a27)
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380abb', 500.00, 4.9, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a83', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a27'), -- Pepsi Cooler
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380abc', 1200.00, 4.7, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a84', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a27'), -- GE Washing Machine

  -- Usuario: Emmett Shear (user_id: a28)
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380abd', 1800.00, 4.6, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a85', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a28'), -- Samsung Smart Refrigerator
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380abe', 400.00, 4.3, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a86', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a28'), -- PlayStation 5

  -- Usuario: Sara Blakely (user_id: a29)
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380abf', 1500.00, 4.8, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a87', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a29'), -- Alienware Aurora R14
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380ac0', 999.99, 4.7, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a88', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a29'), -- Dell XPS 13

  -- Usuario: Whitney Wolfe Herd (user_id: a30)
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380ac1', 109.99, 4.4, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a90', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a30'), -- Nike Air Max 97
  ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380ac2', 120.00, 4.5, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a91', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a30'); -- Adidas Ultraboost 21