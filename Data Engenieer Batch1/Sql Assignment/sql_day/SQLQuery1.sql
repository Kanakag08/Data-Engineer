--- DDL Command create,drop,truncate,alter
create database sql_d;
use sql_d;

create table customers       ---create Command
(
customerID int primary key,
customerName varchar(50),
contactName varchar(50),
address varchar(50)
);

alter table customers       --- alter Command
add pincode varchar(50);

alter table customers      --- drop command
drop column pincode;

truncate table customers;   ---truncate Command

select * from customers;

insert into customers(customerID,customerName,contactName,address)
values
(1,'Alfreds Futterkiste','Maria Anders','Obere Str. 57'),
(2,'Ana Trujillo Emparedados y helados','Ana Trujillo','Avda. de la Constitución 2222'),
(3,'Antonio Moreno Taquería','Antonio Moreno','Mataderos 2312'),
(4,'Around the Horn','Thomas Hardy','120 Hanover Sq.'),
(5,'Berglunds snabbköp','Christina Berglund','Berguvsvägen 8');



---DML Commands select,insert,update,delete

create table employee
(
id int primary key,
name varchar(50),
age int,
state varchar(50),
salary decimal,
customerID int foreign key
references customers(customerID)
);

select name,
Rank () over (
order by name 
) As rank_no
from employee;

select ROW_NUMBER() OVER (
ORDER BY id
) row_num,
name
FROM employee;

select 
DENSE_RANK() over (partition by salary order by age desc) as rank,
salary,age,name
from employee order by salary,age desc;

SELECT id,
NTILE (3) OVER (
ORDER BY id
) Group_number
FROM employee; 

select * from employee;

SELECT COUNT(CustomerID), country
FROM employee
GROUP BY country
HAVING COUNT(CustomerID) > 3;


SELECT id, name, state
FROM employee
WHERE order_delivered_carrier_date IS NULL;


CREATE PROCEDURE us_employee AS
SELECT id, name
FROM employee
WHERE state = 'Delhi';


alter table employee
add customerID int foreign key
references customers(customerID);

update employee           ---update Command
set name='pranshi'        ---set Command
where id =5;

delete from employee      ---delete Command
where id =6;

INSERT INTO employee VALUES               ---insert Command
(1, 'Ramesh', 32, 'Ahmedabad', 2000.00,1),
(2, 'Khilan', 25, 'Delhi', 1500.00,2),
(3, 'Kaushik', 23, 'Kota', 2000.00,3),
(4, 'Chaitali', 25, 'Mumbai', 6500.00,4),
(5, 'Hardik', 27, 'Bhopal', 8500.00,5);

insert into employee values
(6,'kanak',22,'indore',2000.00,1);

select 
C.customerID,
C.customerName,
E.salary,
E.age
from customers as C
Full join employee As E                                  ---join Command
on C.customerID=E.customerID
group by C.customerID,c.customerName,E.salary,E.age;      ---Group By Command


alter table employee
add country varchar(70);



update employee
set country='India'
where id=5;

select * from employee;    ---select Command

insert into employee values
(6,'kanak',22,'Delhi',5000,2,'India');


select customerID,sum(salary)
from employee
group by customerID
having sum(salary)>1000;

SELECT COUNT(CustomerID), Country
FROM employee
GROUP BY Country;

select * from employee
where state ='Delhi' And country='India';

select * from employee
where state in ('Delhi','Bhopal');

select * from employee 
where state not like 'D%';

select * from employee
where state ='Delhi' or country='India';

select * from employee
where state like 'K%';

select * from employee
where id between 1 and 5;

select distinct name from employee;