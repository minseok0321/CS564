WITH user(name) AS (
SELECT DISTINCT(Bidder.User_ID)
FROM Bidder

UNION ALL

SELECT DISTINCT(Seller.User_ID)
FROM Seller)

SELECT COUNT(DISTINCT(user.name))
FROM user;
