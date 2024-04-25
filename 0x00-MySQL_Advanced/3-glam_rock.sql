-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, 
       IF(SPLIT_PART(formed, '-', 1) = 'present', 
          2022 - CAST(SPLIT_PART(formed, '-', 2) AS INTEGER), 
          CAST(SPLIT_PART(split_part(lifespan, '-', 2), ' ', 1) AS INTEGER) - CAST(SPLIT_PART(formed, '-', 1) AS INTEGER)) as lifespan
FROM metal_bands
WHERE split_part(main_style, ', ', 1) = 'Glam rock'
ORDER BY lifespan DESC;
