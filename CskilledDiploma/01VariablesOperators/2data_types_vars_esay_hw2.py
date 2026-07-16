first_student_name = input("Enter the first Student\'s Name: ")
first_student_id = input("Enter the first Student\'s ID: ")
first_student_grade = float(input("Enter the first Student\'s Grade: "))

second_student_name = input("Enter the second Student\'s Name: ")
second_student_id = input("Enter the second Student\'s ID: ")
second_student_grade = float(input("Enter the second Student\'s Grade: "))

print('informat for students and their "math" grades')
print( first_student_name+ "(ID",first_student_id+ ")" , "got grade:",first_student_grade)
print( second_student_name+ "(ID",second_student_id+ ")" , "got grade:",second_student_grade)
print("Average math grade is", (first_student_grade + second_student_grade) / 2)