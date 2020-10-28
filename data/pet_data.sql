CREATE DATABASE PetStore;
use PetStore;
Create table Pets (id int NOT NULL, pet_name varchar(50) NOT NULL, category_id int, category_name varchar(50), pet_status varchar(50), PRIMARY KEY (id));
INSERT INTO Pets values(1021,"Beanny",2,"Snowshoe","available");
INSERT INTO Pets values(1022,"Nana",3,"American Shorthair","sold");
INSERT INTO Pets values(1023,"Momo",4,"Persian","pending");
INSERT INTO Pets values(1024,"Coco",2,"American Shorthair","sold");