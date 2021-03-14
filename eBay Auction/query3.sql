WITH Temp(Item_ID, Count) AS
(SELECT Items.Item_ID, COUNT(Items.Item_ID)
FROM Items
INNER JOIN Category
ON Items.Item_ID = Category. Item_ID
GROUP BY Items.Item_ID)

SELECT COUNT(*)
FROM Temp
WHERE Count = 4;
