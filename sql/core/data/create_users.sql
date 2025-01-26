-- Enable pgcrypto for UUID generation and password hashing
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

INSERT INTO core."user" 
(id, "name", image, email, phone, "password", active, created_at)
VALUES
-- Reid Hoffman (LinkedIn)
(
    gen_random_uuid(),
    'Reid Hoffman',
    'https://example.com/avatars/linkedin-founder.jpg',
    'reid.hoffman@example.com',
    '+1-555-202-4567',
    crypt('linkedin123', gen_salt('bf', 10)),
    true,
    NOW()
),

-- Paul Graham (Y Combinator)
(
    gen_random_uuid(),
    'Paul Graham',
    'https://example.com/avatars/ycombinator-founder.png',
    'paul.graham@ycombinator.example',
    '+1-650-789-0123',
    crypt('hackernews', gen_salt('bf', 10)),
    true,
    NOW()
),

-- Emmett Shear (Twitch)
(
    gen_random_uuid(),
    'Emmett Shear',
    'https://example.com/avatars/twitch-founder.jpg',
    'emmet.shear@example.com',
    '+1-206-555-9812',
    crypt('twitch2023', gen_salt('bf', 10)),
    true,
    NOW()
),

-- Sara Blakely (Spanx)
(
    gen_random_uuid(),
    'Sara Blakely',
    'https://example.com/avatars/spanx-founder.jpg',
    'sara.blakely@example.com',
    '+1-404-555-1122',
    crypt('spanx1234', gen_salt('bf', 10)),
    true,
    NOW()
),

-- Whitney Wolfe Herd (Bumble)
(
    gen_random_uuid(),
    'Whitney Wolfe Herd',
    'https://example.com/avatars/bumble-ceo.jpg',
    'whitney@bumble.example',
    '+1-512-555-3344',
    crypt('bumblebee', gen_salt('bf', 10)),
    true,
    NOW()
);

-- Remaining entrepreneurs follow the same pattern...