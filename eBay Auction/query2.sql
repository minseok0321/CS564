WITH user(name) AS (
SELECT DISTINCT(Bidder.User_ID)
FROM Bidder
WHERE Bidder.Location = "New York"

UNION ALL

SELECT DISTINCT(Seller.User_ID)
FROM Seller
WHERE Seller.Location = "New York")

SELECT COUNT(DISTINCT(user.name))
FROM user;
