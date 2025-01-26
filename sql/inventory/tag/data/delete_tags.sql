-- Eliminación de las etiquetas insertadas en inventory.tag
DELETE FROM inventory.tag
WHERE "name" IN (
  'New Arrival',
  'Discount',
  'Best Seller',
  'Limited Edition',
  'Eco-Friendly',
  'Handmade',
  'Premium Quality',
  'Luxury',
  'Affordable',
  'Trending',
  'Exclusive',
  'Popular',
  'Family-Friendly',
  'For Kids',
  'Seasonal',
  'Outdoor Use',
  'Indoor Use',
  'Durable',
  'Portable',
  'Smart Device',
  'Refurbished',
  'Wireless',
  'Waterproof',
  'Energy Efficient',
  'Customizable'
);