INSERT INTO inventory.product (id, "name", brand_id, product_type_id)
VALUES
  -- Productos para Electronics
  (gen_random_uuid(), 'Coca-Cola Vending Machine', '5fb93a04-fb89-4dcf-955e-dcae17d68b4e', '0cd7414b-a3e6-42b7-9c47-5f6f72df10aa'),
  (gen_random_uuid(), 'Sprite Cooling Dispenser', '3265516c-f372-453d-8225-82c084c5da64', '0cd7414b-a3e6-42b7-9c47-5f6f72df10aa'),
  (gen_random_uuid(), 'Pepsi Cooler', 'be6c0f57-b97f-4d67-b88e-de212989502f', '0cd7414b-a3e6-42b7-9c47-5f6f72df10aa'),

  -- Productos para Home Appliances
  (gen_random_uuid(), 'GE Washing Machine', '85364db2-a721-4c22-a841-21b3285bb822', 'cdf014e7-370f-4e19-964e-7b63a2e1faf9'),
  (gen_random_uuid(), 'Samsung Smart Refrigerator', '3a59e8a6-ca69-41b6-8751-d659199e8630', 'cdf014e7-370f-4e19-964e-7b63a2e1faf9'),

  -- Productos para Gaming Consoles
  (gen_random_uuid(), 'PlayStation 5', 'ac8a110c-177c-4404-8b1e-96a9901f772b', 'db9e85b1-470c-4675-822d-dc4c9d50d027'),
  (gen_random_uuid(), 'Alienware Aurora R14 Gaming Desktop', '3fac09ce-94c4-458a-b49b-96736d1c5f23', 'db9e85b1-470c-4675-822d-dc4c9d50d027'),

  -- Productos para Laptops
  (gen_random_uuid(), 'Dell XPS 13', '0f95923e-2d39-4abf-a440-f2786d70f6fc', '3b7c3157-93c8-4ff5-a45b-e7e7e9094127'),
  (gen_random_uuid(), 'HP Pavilion 15', 'f8d897a6-8ee5-468f-ac70-9654bf132507', '3b7c3157-93c8-4ff5-a45b-e7e7e9094127'),

  -- Productos para Shoes
  (gen_random_uuid(), 'Nike Air Max 97', '81f2459e-a93f-465e-a9a3-32da0a121be5', '9e643cf0-a647-4eac-81ba-98a3737507e2'),
  (gen_random_uuid(), 'Adidas Ultraboost 21', '75315ac6-816d-46ae-8078-7c1b45f0980c', '9e643cf0-a647-4eac-81ba-98a3737507e2');