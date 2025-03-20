'''
Problem Statement:
A university is implementing a Student Enrollment System to manage student registrations for courses

The system must efficiently handle:

Student Registration – Each student has a unique ID, name, and enrolled courses.
Course Enrollment – Students can register for multiple courses. Each course has a name and a maximum capacity.
Efficient Searching – The system should allow checking if a student is enrolled in a course.
Handling Dropouts – Students can drop a course.
Constraints:
The system should be fast for searching and adding students.
Each student can enroll in at most 5 courses.
A course has a maximum capacity of 30 students.


'''

students = {
    'A001': ['Thabo Sibisi', ['Math', 'Physics']],
    'A002': ['Busani Mbatha', ['Pyschology', 'Art']],
    'A003': ['Brenda Mshengula', ['Human Resources', 'Business Studies']]
}

def add_student(students, student_id, name, courses):

    if len(students) >= 30:
        print('The system has reached its maximum capacity (30)')
        return students


    if len(courses) > 5:
        print('A student can only enroll in up to 5 courses.')
        return students
    
    #since we used key value pairs(dictionaries) to make each student unique from each other hence this is the fast way to add it:

    students[student_id] = [name, courses]
    print(f'Student {name} added successfully!')

    return students


students = add_student(students, 'A004', "Samukelisiwe Zulu", ["English", "IsiZulu"])

students = add_student(students, 'A005', "John Doe", ["Math", "Physics", "History", "Chemistry", "Computer Science", "Art"])  # This should trigger the course limit warning
    

print(students)