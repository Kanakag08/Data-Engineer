create database sql_2;
use sql_2;

create table product
(
productID int primary key,
productName varchar(50),
supplierID int foreign key
references supplier(supplierID),
categoryID int,
price int
);
select * from product;

select * from product 
order by price desc
limit 2;

select count(*)
from product;

select avg(price)
from product;

insert into product values
(1,'Chais',1,1,18),
(2,'Chang',1,1,19.5),
(3,'Aniseed Syrup',1,2,20),
(4,'Chef Antons Cajun Seasoning',2,2,22),
(5,'Chef Antons Gumbo Mix',2,2,25);


alter table product 
add unit varchar(70);

update product
set unit='36 boxes'
where productID=5;

insert into product(productID,productName,supplierID,categoryID,unit,price)
values
(6,'Grandmas Boysenberry Spread',3,	2,'12 - 8 oz jars',	25),
(7,'Uncle Bobs Organic Dried Pears',3,7,'12 - 1 lb pkgs.',30),
(8,'Northwoods Cranberry Sauce',3,2,'12 - 12 oz jars',40),
(9,'Mishi Kobe Niku',4,6,'18 - 500 g pkgs.',97);


create table supplier
(
supplierID int primary key,
supplierName varchar(50),
contactName varchar(50),
address varchar(70)
);

insert into supplier values
(1,'Exotic Liquid','Charlotte Cooper','49 Gilbert St.'),
(2,'New Orleans Cajun Delights','Shelley Burke','P.O. Box 78934'),
(3,'Grandma Kellys Homestead','Regina Murphy','707 Oxford Rd.'),
(4,'Tokyo Traders','Yoshi Nagase','9-8 Sekimai Musashino-shi');

SELECT SupplierName
FROM Supplier
WHERE EXISTS (SELECT ProductName FROM Product WHERE Product.SupplierID = Supplier.supplierID AND Price <= 30);

create table orderDetails
(
orderDetaillsID int primary key,
orderID int,
productID int foreign key
references product(productID),
quantity int
);

insert into orderDetails values
(1,10248,1,12),
(2,10248,2,10),
(3,	10248,3,5),
(4,10249,4,9),
(5,	10249,5,40),
(6,10250,6,10),
(7,	10250,7,35),
(8,10250,8,15),
(9,	10251,9,6),
(10,10251,8,15);

select sum(quantity)
from orderDetails;

select * from orderDetails;


select product.productName,orderDetails.orderDetaillsID,orderDetails.quantity
from product,orderDetails
where product.productID < orderDetails.orderDetaillsID;


SELECT productName
FROM Product
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10)


SELECT ProductName
FROM Product
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 1);



create table car_list_price
(
 car_make varchar(60),
 car_model varchar(60),
 car_type varchar(60),
 car_price int
 );

 insert into car_list_price values
 ('Ford','Mondeo','premium',18200),
 ('Renault','Fuego','sport',16500),
('Citroen','Cactus','premium',19000),
('Ford'	,'Falcon','low cost',8990),
('Ford','Galaxy','standard',12400),
('Renault',	'Megane','standard',14300),
('Citroen','Picasso','premium',23400);

select * from car_list_price;

SELECT
    car_make,
    car_model,
    car_price,
    AVG(car_price) OVER() AS "overall average price",
    AVG(car_price) OVER (PARTITION BY car_type) AS "car type average price"
FROM car_list_price;


select 
car_make, car_model ,car_price,
Sum(car_price) over() As "Total Salary"
from car_list_price;

select 
car_make,
sum(car_price) AS total_salary
from car_list_price
group by car_make;