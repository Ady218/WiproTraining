
create database saucedemodb;

use saucedemodb;

create table login(username varchar(20), password int);

alter table login modify username varchar(25) unique;
alter table login modify password varchar(25);

desc login;

insert into login values('admin', 'admin');
insert into login values('standard_user', null);
insert into login (username) values ('error_user');
insert into login (username) values ('visual_user');

select * from login;

update login set password = 'secret_sauce' where username = 'standard_user';
update login set password = 'secret_sauce' where username = 'error_user';

delete from login where username = 'visual_user';

select password as "pwd" from login;

select password as "pwd"from login where username = 'admin';

create database employeedb;
use employeedb;
create table employee(
eid int primary key,
ename varchar(25) not null,
salary numeric(10,2),
bonus numeric(7,2)
);

desc employee;

select * from employee
