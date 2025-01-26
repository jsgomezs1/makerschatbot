-- Delete all inserted consumer product companies
DELETE FROM core.stakeholder
WHERE name IN (
    'The Coca-Cola Company',
    'PepsiCo Inc.',
    'Unilever PLC',
    'Procter & Gamble Co.',
    'Nestlé S.A.',
    'Dell Technologies',
    'HP Inc.',
    'Samsung Electronics',
    'Sony Corporation',
    'Nike, Inc.',
    'Adidas AG',
    'L''Oréal S.A.',  -- Note the escaped apostrophe
    'General Electric',
    'Philips',
    'Intel Corporation'
);

-- Optional: Verify deletion
SELECT * FROM core.stakeholder 
WHERE name IN (...above list...);