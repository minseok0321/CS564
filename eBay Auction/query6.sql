SELECT COUNT(DISTINCT(Seller.User_ID))
FROM Seller, Bidder
WHERE Seller.User_ID = Bidder.User_ID;
