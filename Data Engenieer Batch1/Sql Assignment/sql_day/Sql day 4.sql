create database snowflake;
use snowflake;

create table salestable
(
product_id int not null primary key, 
order_id int not null, 
customer_id int not null, 
employeer_id int not null, 
total int not null , 
Quantity int not null, 
discount int );

create table time_dimension
(
order_id int not null primary key,
order_date date not null);

create table customer_dimension
(customer_id int not null primary key, 
city_id int not null, 
customer_name char(30) not null, 
address varchar(50) not null, 
city char(25) not null, 
zip int not null);

create table product_dimension
(
product_id int not null primary key, 
Product_name varchar(50) not null , 
product_prize decimal not null);


create table emp_dimension
(employeer_id int not null primary key, 
emp_name varchar(30) not null, 
department varchar(25) not null, 
department_id int not null);


create table city_dimension
(city_id int not null primary key,
city_name char(30) not null, 
state char(25), country char(20)
);

create table Product_category_dimension
(product_id int not null primary key, 
name varchar(50) not null, 
pro_description varchar(50) not null, 
unit_prize int not null 
FOREIGN KEY (product_id) REFERENCES product_dimension(product_id));


create table department_dimension
(department_id int, 
department varchar(25) not null, 
location varchar(25) not null);


select * from salestable;

select * from time_dimension;

select * from customer_dimension;

select * from product_dimension;

select * from emp_dimension;

select * from city_dimension;

select * from Product_category_dimension;

select * from department_dimension;






CREATE TABLE SalesList
(
SalesMonth NVARCHAR(20),
SalesQuartes  VARCHAR(5), 
SalesYear  SMALLINT, 
SalesTotal MONEY);

INSERT INTO  SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'March','Q1',2019,60);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'March','Q1',2020,50);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal)
VALUES (N'May','Q2',2019,30);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'July','Q3',2020,10);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'November','Q4',2019,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'October','Q4',2019,150);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'November','Q4',2019,180);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'November','Q4',2020,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'July','Q3',2019,160);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) 
VALUES (N'March','Q1',2020,170);



SELECT  * FROM SalesList;

SELECT CASE 
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'Grand Total'
ELSE
CAST(SalesYear AS varchar(10)) 
END AS SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal 
FROM SalesList
GROUP BY ROLLUP(SalesYear,SalesQuartes);


create table sensor_1
(
id int primary key,
make varchar(50),
city varchar(50)
);


insert into sensor_1
values
(1,	'Honeywell','New York'),
(2,'United Automation','Miami'),
(3,'Omron','Miami'),
(4,'Honeywell','San Francisco'),
(5,'Omron','Boston'),
(6,'RS Pro','Boston');

create table sensor_2
(
id int primary key,
make varchar(50),
city varchar(50));

insert into sensor_2
values
(1,	'Honeywell','San Francisco'),
(2,'United Automation','Boston'),
(3,'eberle','New York'),
(4,'Honeywell','Boston'),
(5,'Omron','Boston'),
(6,'RS Pro','Boston');

select * from sensor_1
Intersect
select * from sensor_2;