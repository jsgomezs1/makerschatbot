-- Keep pgcrypto for password hashing
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

INSERT INTO core."user" 
(id, "name", image, email, phone, "password", active, created_at)
VALUES
-- Reid Hoffman (LinkedIn)
(
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a26',  -- Fixed UUIDv4
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
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a27',  -- Fixed UUIDv4
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
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a28',  -- Fixed UUIDv4
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
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a29',  -- Fixed UUIDv4
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
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a30',  -- Fixed UUIDv4
    'Whitney Wolfe Herd',
    'https://example.com/avatars/bumble-ceo.jpg',
    'whitney@bumble.example',
    '+1-512-555-3344',
    crypt('bumblebee', gen_salt('bf', 10)),
    true,
    NOW()
);