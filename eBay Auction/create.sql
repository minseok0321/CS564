DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Seller;
DROP TABLE IF EXISTS Bidder;

CREATE TABLE Items(
  Item_ID CHAR(50) NOT NULL PRIMARY KEY,
  Item_Name CHAR(50) NOT NULL,
  Buy_Price REAL,
  First_Bid REAL NOT NULL,
  Currently REAL NOT NULL,
  Number_of_Bids INT NOT NULL,
  Started CHAR(50) NOT NULL,
  Ends CHAR(50) NOT NULL,
  Description CHAR(5000)
);

CREATE TABLE Category(
  Item_ID CHAR (50) NOT NULL,
  Category_Name CHAR(50) NOT NULL,
  PRIMARY KEY(Item_ID, Category_Name)
);

CREATE TABLE Seller(
  Item_ID CHAR (50) NOT NULL,  
  User_ID CHAR(50) NOT NULL,
  Rating INT NOT NULL,
  Location CHAR(50),
  Country CHAR(50),
  FOREIGN KEY (Item_ID) REFERENCES Items(Item_ID),
  PRIMARY KEY(Item_ID, User_ID)
);

CREATE TABLE Bidder(
  Item_ID CHAR (50) NOT NULL,  
  User_ID CHAR(50) NOT NULL,
  Rating INT NOT NULL,
  Location CHAR(50),
  Country CHAR(50),
  Time CHAR(50),
  Amount INT NOT NULL,
  FOREIGN KEY (Item_ID) REFERENCES Items(Item_ID),
  PRIMARY KEY (Item_ID, User_ID, Amount)
);

