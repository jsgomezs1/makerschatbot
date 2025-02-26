-- Delete ONLY the brands we inserted in our previous transaction
DELETE FROM inventory.brand
WHERE (name, stakeholder_id) IN (
    -- Coca-Cola Brands
    ('Coca-Cola', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),
    ('Sprite', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),
    ('Fanta', '9fdb173c-b4d2-4927-ae93-70c9d959e591'),
    
    -- PepsiCo Brands
    ('Pepsi', '47bec618-222b-4c52-b037-2cde153f269c'),
    ('Mountain Dew', '47bec618-222b-4c52-b037-2cde153f269c'),
    ('Lays', '47bec618-222b-4c52-b037-2cde153f269c'),
    
    -- Unilever Brands
    ('Dove', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),
    ('Axe', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),
    ('Ben & Jerry''s', 'd0d426fc-81b6-4f62-b9a7-dae8a2bed0eb'),
    
    -- Procter & Gamble Brands
    ('Tide', '78a1b481-10f5-481d-b5cd-faab2472ec99'),
    ('Gillette', '78a1b481-10f5-481d-b5cd-faab2472ec99'),
    ('Oral-B', '78a1b481-10f5-481d-b5cd-faab2472ec99'),
    
    -- Remaining brands from our insert
    ('Nescafé', '5e3adecd-d654-43aa-87b2-74df44354c4a'),
    ('KitKat', '5e3adecd-d654-43aa-87b2-74df44354c4a'),
    ('XPS', '074a90d2-e029-4f37-b720-0092537a8484'),
    ('Alienware', '074a90d2-e029-4f37-b720-0092537a8484'),
    ('Pavilion', 'c19c4101-58f8-4a19-ba88-5f0f0b6c51fd'),
    ('Galaxy', '008252dd-58f0-4d11-99a5-245058c1ac93'),
    ('PlayStation', 'ef2a89c8-07f8-413d-a136-989e5cfc6035'),
    ('Air Max', '6fbe0d13-86b9-407b-8426-aff474e04cad'),
    ('Ultraboost', 'c377c2f1-7ffd-4c1e-93a9-787dbaeb4b08'),
    ('Maybelline', 'edc51ed2-a0ba-43cd-945a-6249a016e004'),
    ('GE Appliances', '6df39ebe-d1ff-44c3-9338-b79e1e75543f'),
    ('Hue Lighting', '0c7da739-3a9e-4079-bb58-8c47daed5e14'),
    ('Core i9', '1d867a0d-db36-46f4-be00-105f5f50cb71')
);

-- Optional: Transaction wrapper for safety
BEGIN;
-- Execute DELETE here
-- Verify with:
SELECT * FROM inventory.brand WHERE (name, stakeholder_id) IN (...);
COMMIT;