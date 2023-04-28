SELECT table_name, table_rows
FROM information_schema.tables
WHERE table_schema = 'inventory'
ORDER BY table_name;

