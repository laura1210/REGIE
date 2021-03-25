# REGIE
This is the final project of MPCS 51410 - Object Oriented Programming.

## Introduction
This project deliverable contains a subset of the [REGIE](https://www.classes.cs.uchicago.edu/archive/2021/winter/51410-1/project.description.html) Course Registration System.  
It covers basic functionalities of student, faculty and administrator actors. For each functionality, there is a separate file to fulfill it and a test file that tests that functionality in depth.  
Python is used as the main programming language and MySQL and MongoDB are used to save data.

## Functionalities Fulfilled in the System
* A student is able to:
    1. Register course (follow the permission requirement and student number limit rules)
    2. Drop course (only when grade has not been assigned)
    3. View course roster
    4. View transcript
    6. Change password

* A faculty is able to:
    1. Approve student's request for a course
    2. View student roster
    3. Send emails to all students
    4. Assign grade
    6. Change password

* An administrator is able to:
    1. Add new course to the course list
    2. Change password

## Use of SOLID Principles in Design
* Single Responsibility Principle:
Each class has a single responsibility which is described by their class name. They serve only one actor and only have one reason to change.

* Interface Segregation Principle:
Interfaces for different group of users are segregated. Student, faculty and administrator entity objects all have their unique interfaces for the functionalities they use. In this way, the users are not dependent on the methods they do not use.

* Dependency Inversion Principle:
High Level Modules which are the test and functionality modules are not dependent on concrete database connections to MySQL and MongoDB. They only depend on abstract database connections which are implemented by ConnSQL.py and ConnMongo.py. In this way, if we want to change our database details, we can do so without any hassle.

* Open/Closed Principle:
By defining clear abstractions for entity objects Student, Course and Faculty, in the domain of a Course Registration System, these entities can be easily extended to include additional methods for other entity objects if needed. It is closed for modification in the sense that we need not change it in order to extended it.

## Use of Design Patterns
* Singleton:
The database connection has been implemented using the Singleton pattern. There should always be only one instance of database connection at any time. All test classes create an instance of Database Connection and pass that instance to the dependent sub-classes and do not let the sub-classes create their own instance of Database Connection. In this way, only one class can modify the database at a given execution.

* State:
We want the course to have 2 states. Course is in open state when the number of current students in the course is less than its student number limit and allows students to register for the course. Course is in closed state when the number of students has exceeded its limit and students can only be added to the waitlist for the course.

## File Structure
* diagram: UML diagrams to show the design of the project
	* faculty_activity.jpg: Adtivity diagram for faculty.
	* faculty_context.jpg: Context map for faculty.
	* permission_sequence.jpg: Sequence diagram for instructor to permit request.
	* register_sequence.jpg: Sequence diagram for student to register a course.
	* student_activity.jpg: Adtivity diagram for student.
	* student_context.jpg: Context map for student.
	* usecase.jpg: Use case for the whole system.

* db: Initialization of databases
    * mysql_initial.sql: Initialize MySQL database to save course, student, faculty, administrator and grade data.
    * mongo_initial.js: Initialize MongoDB database to save the course registration status data.

* code: Python scripts to fulfill the system and tests for each functionality
    * AddCourse.py: Add a new course to the course list.
    * AddCourseTest.py: Tests of add course functionality.
    * Administrator.py: Represent an administrator object.
    * ApproveRequest.py: Approve a student's request of a permission-required course.
    * ApproveRequestTest.py: Tests of approve request functionality.
    * AssignGrade.py: Assign or change grade for a course of a student.
    * AssignGradeTest.py: Tests of assign grade functionality.
    * ChangePass.py: Change password.
    * ChangePassTest.py: Tests of change password functionality.
    * ConnMongo.py: Connection to MongoDB.
    * ConnSQL.py: Connection to MySQL.
    * Course.py: Represent a course object.
    * DropCourse.py: Drop a course.
    * DropCourseTest.py: Tests of drop course functionality.
    * Faculty.py: Represent a faculty object.
    * FacultyCheck.py: Check if a faculty is instructor for a course. This can be used by many other functionalities for a faculty to modify a course.
    * RegisterCourse.py: Register for a course.
    * RegisterCourseTest.py: Tests of register course.
    * SendEmail.py: Send emails to all enrolled students.
    * SendEmailTest.py: Tests of send emails.
    * Student.py: Represent a student object.
    * ViewCourse: View course list.
    * ViewCourseTest: Tests of view course list.
    * ViewStudent: View student roster for a course.
    * ViewStudentTest: Tests of view student roster.
    * ViewTranscript: View transcript including all courses.
    * ViewTransTest: Tests of view transcript.

For more details, please check the comments in each script.