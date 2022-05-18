create database staff1;
use staff1;
create table department(
dep_id varchar(30) primary key,
dep_name varchar(30));

create table staff(
staff_id varchar(30) primary key,
designation varchar(30),
qualification varchar(30),
type_of_appointment varchar(30),
dep_id varchar(30),
salary int,
foreign key (dep_id) references department(dep_id));

desc department;
desc staff;

 insert into department values
 ('100','MCA'),
 ('101','CSE'),
 ('102','BCA');
 
 insert into staff values
 ('001','Proff','Doct','Perm','100','100000'),
 ('002','Teacher','PG','Perm','101','75000'),
 ('003','Teaching Assistent','UG','Guest','102','50000'),
 ('004','Proff','Doct','Guest','100','75000'),
 ('005','Lab Staff','UG','Guest','101','50000'),
 ('006','Teacher','UG','Perm','102','150000');
 
 /* Find number of guest faculty in each dept*/
 select count(*),dep_name from staff,department where staff.dep_id=department.dep_id and type_of_appointment="Guest" group by dep_name;
 
 /*Find the department maximum number of staff having doctorate*/
 select dep_name from department,staff where staff.dep_id=department.dep_id AND qualification="Doct" group by dep_name order by count(dep_name) desc limit 1;
 
 /*Find the average salary of guest employee in eaxh department*/
 select avg(salary), dep_name from staff,department where staff.dep_id=department.dep_id AND type_of_appointment="Guest" group by dep_name;
 
 /*Find the number of faculties who have max salary*/
 select max(salary), dep_name from staff,department where staff.dep_id=department.dep_id group by dep_name;
 
 /*Find the total salary of MCA department*/
 select sum(salary) from staff,department where staff.dep_id =department.dep_id AND dep_name="MCA";
 
 
 select * from staff;
 select * from department;
 