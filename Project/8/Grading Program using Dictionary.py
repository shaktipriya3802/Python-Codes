# Student Grading Criteria
#   - Scores 91 - 100: Grade = "Outstanding" 
#   - Scores 81 - 90: Grade = "Exceeds Expectations" 
#   - Scores 71 - 80: Grade = "Acceptable" 
#   - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

grade="" # Creating an Empty String to hold the value
student_grades={} # Creating an Empty Dictionary 

for key in student_scores: # Setting Student Grading Criteria 
    a=student_scores[key]
    if a>70 and a<=80:
        grade = "Acceptable"
    elif a>80 and a<=90:
        grade = "Exceeds Expectations"
    elif a>90 and a<=100:
        grade = "Outstanding"
    else:
        grade = "Fail"
    
    # Prints the Student Name, Score & Grade Obtained 
    print("Name:", key, "Score =", student_scores[key], "Grade =", grade) 
    
    student_grades[key]=grade # Adds Student Name & Grade obtained to the Empty String 

# Printing the Empty Dictionary that holds Student's Name & their Grades
print(student_grades) 

