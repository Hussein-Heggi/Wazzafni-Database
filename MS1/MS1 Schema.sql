CREATE DATABASE IF NOT EXISTS Job_Finder;
USE Job_Finder;

CREATE TABLE IF NOT EXISTS Users
(
Email varchar(50) PRIMARY KEY,
Username varchar(20) not NULL, 
Gender char(1) not NULL,
Birth_Date date not NULL,
GPA decimal(3,2) not NULL
);

CREATE TABLE IF NOT EXISTS Organizations
(
Comp_Name varchar(50) PRIMARY KEY,
Size int not NULL,
Area varchar(20),
City varchar(20) not NULL,
Country varchar (30) not NULL, 
Foundation_Date date not NULL,
Comp_Description text,
URL varchar(200) 
);

CREATE TABLE IF NOT EXISTS Organizations_Sector
(
Comp_Name varchar(50) not NULL,
Sector varchar(50) not NULL,
PRIMARY KEY (Comp_Name, Sector),
FOREIGN KEY (Comp_Name) References Organizations(Comp_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Skill
(
Skill_Name varchar(25) PRIMARY KEY 
);

CREATE TABLE IF NOT EXISTS Category
(
Category_Name varchar(25) PRIMARY KEY 
);

CREATE TABLE IF NOT EXISTS Job_Post
(
Comp_Name varchar(25) not NULL,
Title varchar(20) not NULL,
City varchar(20) not NULL,
Area varchar(20),
Country varchar (30) not NULL, 
Date_Posted date not NULL,
Job_Description text not NULL,
Vacancies int not NULL,
Experience varchar(20),
Career_Level varchar(30),
Education_Level varchar(30),
Min_Salary int not NULL,
Max_Salary int not NULL,
PRIMARY KEY (Comp_Name, Title, City),
FOREIGN KEY (Comp_Name) References Organizations(Comp_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Job_Type
(
Comp_Name varchar(50) not NULL,
Title varchar(20) not NULL,
City varchar(20) not NULL,
Job_Type varchar(20) not NULL,
PRIMARY KEY (Comp_Name, Title, City, Job_Type),
FOREIGN KEY (Comp_Name, Title, City) References Job_Post(Comp_Name, Title, City) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Apply
(
Comp_Name varchar(50) not NULL,
Job_Title varchar(20) not NULL,
City varchar(20) not NULL,
User_Email varchar(50) not NULL,
Application_Date date not NULL,
Cover_Letter text,
PRIMARY KEY (Comp_Name, Job_Title, City, User_Email),
FOREIGN KEY (Comp_Name, Job_Title, City) References Job_Post(Comp_Name, Title, City) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (User_Email) References Users(Email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Acquire
(
User_Email varchar(50) not NULL,
Skill_Name varchar(25) not NULL,
PRIMARY KEY (User_Email, Skill_Name),
FOREIGN KEY (Skill_Name) References Skill(Skill_Name) ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (User_Email) References Users(Email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Requires
(
Comp_Name varchar(50) not NULL,
Job_Title varchar(20) not NULL,
City varchar(20) not NULL,
Skill_Name varchar(25) not NULL,
PRIMARY KEY (Comp_Name, Job_Title, City, Skill_Name),
FOREIGN KEY (Skill_Name) References Skill(Skill_Name) ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (Comp_Name, Job_Title, City) References Job_Post(Comp_Name, Title, City) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Under
(
Comp_Name varchar(50) not NULL,
Job_Title varchar(20) not NULL,
City varchar(20) not NULL,
Category_Name varchar(25) not NULL,
PRIMARY KEY (Comp_Name, Job_Title, City, Category_Name),
FOREIGN KEY (Category_Name) References Category(Category_Name) ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (Comp_Name, Job_Title, City) References Job_Post(Comp_Name, Title, City) ON DELETE CASCADE ON UPDATE CASCADE
);

