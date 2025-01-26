BEGIN;

DELETE FROM core."user"
WHERE "name" IN (
    'Reid Hoffman',
    'Paul Graham',
    'Emmett Shear',
    'Elon Musk',
    'Mark Zuckerberg',
    'Brian Chesky',
    'Sara Blakely',
    'Whitney Wolfe Herd',
    'Tristan Walker'
);

-- Verify deletion before committing
SELECT * FROM core."user" WHERE "name" IN (...the same list...);

COMMIT;
-- ROLLBACK;  -- Use if verification shows unexpected results