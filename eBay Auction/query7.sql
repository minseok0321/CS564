SELECT COUNT(DISTINCT Category.Category_Name)
FROM Category, Bidder
WHERE Category.Item_ID = Bidder.Item_ID
AND Bidder.Amount > 100;
