SELECT table_name as chennel
     , table_rows as count
FROM information_schema.tables
WHERE table_schema = 'inventory'
ORDER BY table_name;

