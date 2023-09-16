

from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Set grades achieved so far
my_grades.quiz_1 = 0.78 # Received 78% in the first quiz
my_grades.quiz_2 = 0.6 # Received 60% in the second quiz
my_grades.midterm = 0.8 # Received 80% in the midterm

# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')

# Calculate minimum average grade needed in ungraded assignments to get an A in the course
minimum_average_percentage_grade = GradeCalculator.calculate_optimistic_minimum_average_grade(my_grades, weights)
minimum_average_letter_grade = GradeCalculator.calculate_letter_grade(minimum_average_percentage_grade)
print(f'To get an A in the course, you will need a minimum of {round(minimum_average_percentage_grade*100, 2)}% in all ungraded assignments, which is a {minimum_average_letter_grade}.')