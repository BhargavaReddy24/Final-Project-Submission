from in_memory_database import InMemoryDatabase

# Create an in-memory database and insert some sample data
database = InMemoryDatabase()
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