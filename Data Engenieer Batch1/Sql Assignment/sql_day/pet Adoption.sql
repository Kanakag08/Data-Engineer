create database pet_adoption;
use pet_adoption;

---create table animal

create table animals
( 
id int primary key,
name varchar(50),
breed varchar(50),
color varchar(50),
gender varchar(50),
status int
);

---insert data for dog only

insert into animals values
(1,'Bellyflop','Beagle','Brown','Male',1),
(2,'snowy','Husky','White','Female',0),
(3,'Princess','Pomeranian','Balck','Female',1),
(4,'Cricket','Chihuauhua','Brown','Male',1),
(5,'Princess','poodle','Purple','Female',0),
(6,'Spot','Daimation','balck and White','Male',1);

SELECT * FROM animals;

SELECT breed FROM animals;

SELECT name FROM animals WHERE gender = 'Female';

SELECT id FROM animals WHERE status = 0;

UPDATE animals 
SET color = 'Brown' 
WHERE id = 3;

UPDATE animals 
SET color = 'Brown' 
WHERE name = 'Princess';


UPDATE animals 
SET status = 1
WHERE id = 5;

---added new column species

ALTER TABLE animals 
ADD species varchar(70);

UPDATE animals 
SET species = 'Dog';

SELECT * FROM animals;

delete from animals
where id=103;


---inserted data for cat also

insert into animals(id,name,breed,color,gender,status,species)
values
(7, 'Meowmix','Munchkin', 'Yellow', 'Female', 0,'cat'),
(8,'Ash','Persian', 'Gray', 'Female', 0,'cat'),
(9,'Tiger','Bengal', 'Brown', 'Male', 0,'cat');

---Added new column named as Shelter

ALTER TABLE animals 
ADD shelter INT;

UPDATE animals 
SET shelter = 1;


--- added new database in animals after adding new columns like shelter,species

INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) 
VALUES 
(10, 'Snoops', 2, 'Dog', 'Beagle', 'Brown', 'Male', 0),
(11, 'Salt', 2, 'Cat', 'Turkish Angora', 'White', 'Female', 0),
(12,'Fuzz', 3, 'Dog', 'Papillon', 'Gray', 'Male', 0);


---created index on shelter 

CREATE INDEX animal_shelter 
ON animals (shelter);


---Joining animal table with shelter table

SELECT * FROM animals 
JOIN shelters 
ON animals.shelter = shelters.id;



--- joinning the adoption table with animal table 

SELECT * FROM adoptions 
JOIN animals 
ON adoptions.animal_id = animals.id 
WHERE animals.shelter = 1;





---create table adoptions

create table adoptions
(
animal_id int foreign key 
references animals(id),
name varchar(50),
contact int,
date date
);

alter table adoptions
drop column date;

alter table adoptions
add edate date;

select * from animals;

SELECT id, name, COUNT(*)
FROM animals
GROUP BY id, name
HAVING COUNT(*) > 1;

select *from adoptions;

insert into adoptions values
(1,'Princess the Poodle','poodlequeen@cockroachlabs .com','2024-1-21'),
(2,'Spot the Dalmation','pellacrew@cockroachlabs.com','2023-12-18');

SELECT * FROM adoptions 
ORDER BY edate DESC;

---new Table Shelter

CREATE TABLE shelters 
(
id Int, 
name varchar(50), 
location varchar(50)
);

INSERT INTO shelters (id, name, location) 
VALUES 
(1, 'Animals 4 Homes', 'Red City');

insert into shelters values
(2, 'Adopt A Buddy', 'Green Town'),
(3, 'Fluffy Animals', 'Blue Hills');

select * from shelters;

select CONCAT ('Kanak Agrawal','@gmail.com');








---creating table user

create table USERS
(NAME char(20),
BREEDTYPE char(20), 
PRIZE varchar(20)
);
INSERT INTO USERS VALUES('ABHIRAM','GERMAN',30000);
INSERT INTO USERS VALUES('SURESH','GOLDEN',40000);
INSERT INTO USERS VALUES('RAMESH','GERMAN',25000);
insert into USERS(NAME,PRIZE) 
values 
('KANAK',50000);

---create table for animals list

CREATE TABLE ANIMALSLIST
(
id VARCHAR(20) NOT NULL, 
name CHAR(20), breed CHAR(20), 
color CHAR(20), 
gender CHAR(20), 
status VARCHAR(20)
);
INSERT INTO ANIMALSLIST VALUES('25484A78', 'SNOOPY','GERMANY','WHITE','MALE','1');
INSERT INTO ANIMALSLIST VALUES('25ACA78', 'DOG1','GOLDEN','BROWN','FEMALE','0');
INSERT INTO ANIMALSLIST VALUES('25CBD78', 'DOG2','GERMAN','BLACK','MALE',1);



SELECT * FROM ANIMALSLIST WHERE gender='MALE';

update ANIMALSLIST SET NAME='BRODDY' WHERE NAME ='DOG2';

UPDATE ANIMALSLIST SET STATUS=1 WHERE ID='25ACA78';

SELECT * FROM USERS ORDER BY PRIZE DESC;

SELECT * FROM USERS ORDER BY PRIZE ;

UPDATE ANIMALSLIST SET STATUS=0 WHERE ID='25ACA78';

SELECT * FROM ANIMALSLIST ORDER BY STATUS;

select * from USERS;

SELECT NAME, PRIZE, BREEDTYPE
FROM USERS
WHERE BREEDTYPE IS NULL;

SELECT COALESCE(NULL, 1, 2, 'Kanak.com');


