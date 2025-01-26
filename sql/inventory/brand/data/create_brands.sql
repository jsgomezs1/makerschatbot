INSERT INTO inventory.brand (id, name, stakeholder_id)
VALUES
-- Coca-Cola Brands
(gen_random_uuid(), 'Coca-Cola', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),
(gen_random_uuid(), 'Sprite', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),
(gen_random_uuid(), 'Fanta', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),

-- PepsiCo Brands
(gen_random_uuid(), 'Pepsi', '47bec618-222b-4c52-b037-2cde153f269c'),
(gen_random_uuid(), 'Mountain Dew', '47bec618-222b-4c52-b037-2cde153f269c'),
(gen_random_uuid(), 'Lays', '47bec618-222b-4c52-b037-2cde153f269c'),

-- Unilever Brands
(gen_random_uuid(), 'Dove', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),
(gen_random_uuid(), 'Axe', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),
(gen_random_uuid(), 'Ben & Jerry''s', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),

-- Procter & Gamble Brands
(gen_random_uuid(), 'Tide', '78a1b481-10f5-481d-b5cd-faab2472ec99'),
(gen_random_uuid(), 'Gillette', '78a1b481-10f5-481d-b5cd-faab2472ec99'),
(gen_random_uuid(), 'Oral-B', '78a1b481-10f5-481d-b5cd-faab2472ec99'),

-- Continue this pattern for other stakeholders...
(gen_random_uuid(), 'Nescafé', '5e3adecd-d654-43aa-87b2-74df44354c4a'),
(gen_random_uuid(), 'KitKat', '5e3adecd-d654-43aa-87b2-74df44354c4a'),
(gen_random_uuid(), 'XPS', '074a90d2-e029-4f37-b720-0092537a8484'),
(gen_random_uuid(), 'Alienware', '074a90d2-e029-4f37-b720-0092537a8484'),
(gen_random_uuid(), 'Pavilion', 'c19c4101-58f8-4a19-ba88-5f0f0b6c51fd'),
(gen_random_uuid(), 'Galaxy', '008252dd-58f0-4d11-99a5-245058c1ac93'),
(gen_random_uuid(), 'PlayStation', 'ef2a89c8-07f8-413d-a136-989e5cfc6035'),
(gen_random_uuid(), 'Air Max', '6fbe0d13-86b9-407b-8426-aff474e04cad'),
(gen_random_uuid(), 'Ultraboost', 'c377c2f1-7ffd-4c1e-93a9-787dbaeb4b08'),
(gen_random_uuid(), 'Maybelline', 'edc51ed2-a0ba-43cd-945a-6249a016e004'),
(gen_random_uuid(), 'GE Appliances', '6df39ebe-d1ff-44c3-9338-b79e1e75543f'),
(gen_random_uuid(), 'Hue Lighting', '0c7da739-3a9e-4079-bb58-8c47daed5e14'),
(gen_random_uuid(), 'Core i9', '1d867a0d-db36-46f4-be00-105f5f50cb71');