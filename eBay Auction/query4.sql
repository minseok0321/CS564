SELECT Item_ID
FROM Items
WHERE Currently = (SELECT MAX(Currently) FROM Items);
