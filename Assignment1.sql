DROP TABLE IF EXISTS [order];
DROP TABLE IF EXISTS [purchase];
DROP TABLE IF EXISTS [supplier];
DROP TABLE IF EXISTS [product];
DROP TABLE IF EXISTS [alert];



CREATE TABLE product (
  [ProductId] int NOT NULL IDENTITY PRIMARY KEY,
  [ProductName] varchar(255) NOT NULL,
  [PartNumber] varchar(255) NOT NULL,
  [ProductLabel] varchar(255) NOT NULL,
  [StartingInventory] int NOT NULL,
  [InventoryReceived] int NOT NULL,
  [InventoryShipped] int NOT NULL,
  [InventoryOnHand] int NOT NULL,
  [MinimumRequired] int NOT NULL,
) ;


SET IDENTITY_INSERT product ON
INSERT INTO product ([ProductId], [ProductName], [PartNumber], [ProductLabel], [StartingInventory], [InventoryReceived], [InventoryShipped], [InventoryOnHand], [MinimumRequired])
VALUES
(1,'keyboard','1','Keyboard-123',0,0,0,200,50),
(2,'Mouse','2','Mouse-123456',0,0,0,200,50),
(3,'Desktop','3','Toby- 57456',0,0,0,200,50),
(4,'Monitor','4','Monitor-1243',0,0,0,200,50),
(5,'Laptop','5','Laptop-342',0,0,0,200,50),
(6,'Sdcard','6','Sdcard-1234',0,0,0,200,50),
(7,'Cables','7','Cables-4333',0,0,0,200,50),
(8,'Pi Camera','8','Pi Camera - 001',0,0,0,200,50),
(9,'Wireless Camera','9','Wireless - 001',0,0,0,200,50);
SET IDENTITY_INSERT product OFF

CREATE TABLE alert(
[AlertId] int NOT NULL IDENTITY(1, 1) PRIMARY KEY,
[ProductId] int NOT NULL, 
[ProductName] varchar(255) NOT NULL,
[AlertType] varchar(50) NULL,
[AlertDate] DateTime null,
[AlertDescription] varchar(255) NULL
);
go
 
drop trigger if exists [StockAlert]
go



CREATE TRIGGER TR_Stock_Alert
ON product
AFTER UPDATE
AS
BEGIN
INSERT INTO alert 
SELECT [ProductID], [ProductName], 'Low Stock', GETDATE(),
'There is only '+cast([InventoryOnHand] as varchar(10))
 + ' ' +[ProductName] + ' left' 
FROM inserted
WHERE [InventoryOnHand] <= [MinimumRequired]
END
GO

/** test purpose
update product set InventoryOnHand = 9 where ProductId=10
select * from alert
**/


 
CREATE TABLE [order] (
  [OrderId] int NOT NULL IDENTITY PRIMARY KEY,
  [Title] varchar(255) NOT NULL,
  [First] varchar(255) NOT NULL,
  [Middle] varchar(255) DEFAULT NULL,
  [Last] varchar(255) NOT NULL,
  [ProductId] int NOT NULL REFERENCES product([productId]),
  [NumberShipped] int NOT NULL,
  [OrderDate] date NOT NULL,
 ) ;

 SET IDENTITY_INSERT [order] ON
INSERT INTO [order] ([OrderId], [Title], [First], [Middle], [Last], [ProductId], [NumberShipped], [OrderDate])
VALUES
(1,'Order1','Eden','','Park',3,10,'2019-07-01'),
(2,'Order2','Ken','','Sutton',3,20,'2019-07-02'),
(3,'Order3','Ben','','Tompson',1,5,'2019-07-03'),
(4,'Order4','Johnny','','Test',3,10,'2019-07-04'),
(5,'Order5','Steve','','Smith',1,20,'2019-07-05'),
(6,'Order6','Jock','','Palmer',3,3,'2019-07-06'),
(7,'Order7','Kaily','','Scott',3,5,'2019-07-07'),
(8,'Order8','Deb','','Boy',3,10,'2019-07-08'),
(9,'Order9','Susan','','Useless',2,30,'2019-07-09'),
(10,'Order10','Eamonn','','Hoppman',3,5,'2019-07-10');
  SET IDENTITY_INSERT [order] OFF


CREATE TABLE supplier (
  [SupplierId] int NOT NULL IDENTITY PRIMARY KEY,
  [SupplierName] varchar(255) NOT NULL 
) ;

SET IDENTITY_INSERT supplier ON
INSERT INTO supplier ([SupplierId], [SupplierName])
VALUES
(1,'Nova Tech'),
(2,'Warehouse'),
(3,'Noel Leeming'),
(4,'Pb Tech'),
(5,'Elis');
SET IDENTITY_INSERT supplier OFF

CREATE TABLE purchase (
  [PurchaseId] int NOT NULL IDENTITY PRIMARY KEY,
  [SupplierId] int NOT NULL REFERENCES supplier(SupplierId),
  [ProductId] int NOT NULL REFERENCES product (ProductId),
  [NumberReceived] int NOT NULL,
  [PurchaseDate] date NOT NULL,
 ) ;

 SET IDENTITY_INSERT purchase ON
INSERT INTO purchase ([PurchaseId], [SupplierId], [ProductId], [NumberReceived], [PurchaseDate])
VALUES
(1,2,2,50,'2014-11-02'),
(2,2,1,15,'2014-09-02'),
(3,3,3,10,'2014-11-12'),
(4,2,2,25,'2014-01-02'),
(5,2,3,20,'2014-02-22'),
(6,1,1,5,'2015-11-02'),
(7,3,3,3,'2014-01-02'),
(8,1,3,20,'2015-11-11'),
(9,2,1,0,'2014-11-02');
 SET IDENTITY_INSERT purchase OFF


 drop trigger if exists TR_Incoming_Stock
 go
 
 
CREATE TRIGGER TR_Incoming_Stock
ON purchase 
AFTER INSERT AS 
BEGIN
DECLARE @Inserted_Value INT, @ProductId INT
SELECT @Inserted_Value = NumberReceived, @ProductId = ProductId from inserted
UPDATE product SET InventoryOnHand = InventoryOnHand + @Inserted_Value, InventoryReceived = InventoryReceived + @Inserted_Value
WHERE ProductId = @ProductId
 END
 GO



 drop trigger if exists TR_Outgoing_stock
 go

 CREATE TRIGGER TR_Outgoing_Stock
 ON [order]
 AFTER INSERT AS
 BEGIN
DECLARE @outgoing_value INT, @ProductId int
SELECT @outgoing_value = NumberShipped, @ProductId = ProductId from inserted
UPDATE product SET InventoryOnHand = InventoryOnHand - @outgoing_value, InventoryShipped = InventoryShipped + @outgoing_value
WHERE ProductId = @ProductId 
 END
 GO

 /*
select * from purchase

select * from product

SET IDENTITY_INSERT purchase ON
INSERT INTO purchase ( [SupplierId], [ProductId], [NumberReceived], [PurchaseDate])
VALUES (2,1,50,'2014-11-02')
SET IDENTITY_INSERT purchase OFF
*/


select * from product
INSERT INTO purchase ( [SupplierId], [ProductId], [NumberReceived], [PurchaseDate])
VALUES (2,1,50,'2014-11-02')
select * from product

 

select * from product


INSERT INTO [order] ( [Title], [First], [Middle], [Last], [ProductId], [NumberShipped], [OrderDate])
VALUES
('Order1','Eden','','Park',1,50,'2019-07-01')

select * from product


 /** testing purpose
 select * from purchase
 select * from [order]
 select  * from product

 

 SET IDENTITY_INSERT purchase ON
 INSERT INTO purchase ([PurchaseId], [SupplierId], [ProductId], [NumberReceived], [PurchaseDate])
VALUES (14,2,1,50,'2014-11-02')
SET IDENTITY_INSERT purchase OFF

SET IDENTITY_INSERT [order] ON
INSERT INTO [order] ([OrderId], [Title], [First], [Middle], [Last], [ProductId], [NumberShipped], [OrderDate])
VALUES
(11,'Order1','Eden','','Park',1,50,'2019-07-01')
SET IDENTITY_INSERT [order] OFF

SELECT * FROM [product]
**/

use inventory
select * from [order]

 