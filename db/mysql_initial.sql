/* Create the REGIE database and tables needed to store information */
create database if not exists REGIE;
use REGIE;

drop table if exists Course;
create table Course(course_code varchar(12) primary key,
                    course_name varchar(80),
                    max_num int(3),
                    classroom varchar(20), 
                    schedule varchar(30),
                    permission_required boolean);

drop table if exists Student;
create table Student(id int(8) primary key, 
                     name varchar(20),
                     password varchar(20),
                     email varchar(100));

drop table if exists Faculty;
create table Faculty(id int(8) primary key, 
                     name varchar(20),
                     password varchar(20),
                     title varchar(30),
                     status varchar(20));

drop table if exists Administrator;
create table Administrator(id int(8) primary key, 
                           name varchar(15), 
                           password varchar(20));

drop table if exists Grade;
create table Grade(course_code varchar(12),
                   student_id int(8), 
                   grade varchar(2) default null,
                   primary key(course_code, student_id));

/* Insert initial data into the REGIE database */
insert into Course values('MPCS_51410','Object Oriented Programming',50,'online','Mon 17:30-20:30',1);
insert into Course values('MPCS_52553','Web Development',50,'online','Thu 19:40-21:00',0);
insert into Course values('PPHA_36800','Higher Education and Public Policy',5,'online','Thu 14:40-17:40',0);
insert into Course values('CAPP_30300','Civic Data & Technology Clinic',20,'online','Wed 10:00-11:00',1);
insert into Course values('MPCS_55001','Algorithms',50,'online','Tue 14:40-16:00',0);
 
insert into Student values(10000000,'Laura Liu','laura_pass','laura@uchicago.edu');
insert into Student values(20000000,'Tony Hu','tony_pass','tony@uchicago.edu');
insert into Student values(30000000,'Ellen Black','ellen_pass','ellen@uchicago.edu');
insert into Student values(40000000,'Steph Taylor','steph_pass','steph@uchicago.edu');
insert into Student values(50000000,'Jane Smith','jane_pass','jane@uchicago.edu');
insert into Student values(60000000,'Colin Wilson','colin_pass','colin@uchicago.edu');

insert into Faculty values(10000000,'Jeffrey Shacklette','jeffrey_pass','professor','parttime');
insert into Faculty values(20000000,'Jeffrey Cohen','jeffrey_pass','professor','parttime');
insert into Faculty values(30000000,'Jennifer Delaney','jennifer_pass','professor','fulltime');
insert into Faculty values(40000000,'Yue Wang','yue_pass','TA','parttime');
insert into Faculty values(50000000,'David Uminsky','david_pass','professor','parttime');
insert into Faculty values(60000000,'Amitabh Chaudhary','amitabh_pass','professor','fulltime');
insert into Faculty values(70000000,'Bill Davies','bill_pass','grader','parttime');

insert into Administrator values(10000000,'Eren Jaeger','eren_pass');
insert into Administrator values(20000000,'Levi Ackerman','levi_pass');

insert into Grade values('CAPP_30300',10000000,'A');
insert into Grade values('MPCS_55001',10000000,'A');
insert into Grade values('CAPP_30300',40000000,'A');