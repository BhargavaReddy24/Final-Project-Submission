This repository contains an SQL "Parser and Interpreter" that can parse and interpret SQL queries. 
The sql_parser.py file contains the code for the Parser.
The sql_interpreter.py file contains the code for Interpreter.
The in_memory_database.py file contains the code for Interpreter.
_____________________________________________________________________________________________________________________________________________________________________
Requirements:

Python 3.6+
lark-parser 0.12.0+
_____________________________________________________________________________________________________________________________________________________________________
Usage:

=> SQL parser can be executed in 2 ways:

1.Copy the Grammar from the sql_parser.py (line 5-72) file in "LARK IDE". A parse tree is generated with desired SQL query of choice.

2.To use the SQL parser, run the sql_parser.py file and enter a SQL query when prompted. The parser will parse the query and print the parsed output.

Example:

Enter a SQL query: SELECT name, teacher FROM courses;
Parsed query: start
  statement
    select_statement
      select_list
        select_list_item
          column_name	name
        select_list_item
          column_name	teacher
      table_name	courses
      end_statement
Process finished with exit code 0
_____________________________________________________________________________________________________________________________________________________________________

=> To use the Interpreter, run the sql_interpreter.py file and enter a SQL query when prompted. The Interpreter will execute the query and displays output.

Example:

Enter a SQL query (or 'quit' to exit): CREATE TABLE users (id INT, name VARCHAR(50));
Table created successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (1, 'Alice');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (2, 'ice');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (3, 'lice');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (4, 'Aice');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (5, 'Alce');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): INSERT INTO users (id, name) VALUES (6, 'Alie');
Record inserted successfully
Enter a SQL query (or 'quit' to exit): SELECT * FROM users;
(1, 'Alice')
(2, 'ice')
(3, 'lice')
(4, 'Aice')
(5, 'Alce')
(6, 'Alie')
Enter a SQL query (or 'quit' to exit): quit

=> To use the Interpreter, run the in_memory-database.py file. There is an sample_data which is pre-defined for an user to give a basic idea of testing the Insert queries.

The sample_data goes like this:

database.insert('students', ['id', 'name', 'age'], [1, 'Alice', 20])
database.insert('students', ['id', 'name', 'age'], [2, 'Bob', 21])
database.insert('students', ['id', 'name', 'age'], [3, 'Charlie', 19])
database.insert('courses', ['id', 'name', 'teacher'], [1, 'Math', 'Mr. Johnson'])
database.insert('courses', ['id', 'name', 'teacher'], [2, 'Science', 'Mrs. Smith'])
database.insert('enrollments', ['id', 'student_id', 'course_id', 'grade'], [1, 1, 1, 'A'])
database.insert('enrollments', ['id', 'student_id', 'course_id', 'grade'], [2, 1, 2, 'B'])
database.insert('enrollments', ['id', 'student_id', 'course_id', 'grade'], [3, 2, 1, 'B'])
database.insert('enrollments', ['id', 'student_id', 'course_id', 'grade'], [4, 2, 2, 'A'])
database.insert('enrollments', ['id', 'student_id', 'course_id', 'grade'], [5, 3, 2, 'C'])
 
__________________________________________________________________________________________________________________________________________________________________
Conclusion:
 
This code defines a grammar for parsing SQL statements with support for joins and DDL statements such as CREATE TABLE, ALTER TABLE, and DROP TABLE. 
The grammar also includes support for data manipulation language (DML) statements such as SELECT, INSERT, UPDATE, and DELETE. 
With this code, you can write SQL queries that perform complex database operations. 

The parser_test_sql_queries.txt file contains some SQL queries that can be used to test the Parser.
The sample_data file contains some SQL queries that can be used to test the Interpreter.