# <202280005@psu.palawan.edu.ph>
# Function 1: Calculate Weighted Average
# Coder1: Mark Cedie Buday @ BSCS2-B1
# Coder2: John Lester Balmaceda @ BSCS2-B1
# Schedule01: T: 11:00-13:00 CE Bldg 15
# Schedule02: F: 10:00-13:00 NIT 1
# Date Created: 2023-08-25
# Added database using sqlite3
import os
class System:
    def __name__(self):
        pass
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
sys0 = System()
sys0.clear()
def calculate_average(list):
    return sum(list) / len(list)
std1_ass = [50, 60, 70, 80, 90, 95, 75]
std1_quiz = [80, 75, 88, 92, 90]
std1_exam = [94]
std2_ass = [45, 99, 100, 100, 88, 75, 95]
std2_quiz = [100, 100, 99, 100, 98]
std2_exam = [94]
std3_ass = [46, 76, 88, 98, 97, 91, 94]
std3_quiz = [81, 82, 83, 84, 85]
std3_exam = [84]
std4_ass = [67, 71, 85, 86, 92, 61, 72]
std4_quiz = [82, 84, 86, 88, 90]
std4_exam = [98]
std5_ass = [50, 74, 87, 92, 94, 96, 100]
std5_quiz = [83, 87, 92, 80, 60]
std5_exam = [82]
assignments = [std1_ass, std2_ass, std3_ass, std4_ass, std5_ass]
quizzes = [std1_quiz, std2_quiz, std3_quiz, std4_quiz, std5_quiz]
exams = [std1_exam, std2_exam, std3_exam, std4_exam, std5_exam]
for i in range(7):
    assignment_scores = [ass[i] for ass in assignments]
    print(f'A{i+1} U: {assignment_scores}')
    print(f'A{i+1} S: {sorted(assignment_scores)}')
    print(f'Class avg: {calculate_average(assignment_scores)}%\n')
for i in range(5):
    quiz_scores = [quiz[i] for quiz in quizzes]
    print(f'Q{i+1} U: {quiz_scores}')
    print(f'Q{i+1} S: {sorted(quiz_scores)}')
    print(f'Class avg: {calculate_average(quiz_scores)}%\n')
for i in range(1):
    exam_scores = [exam[i] for exam in exams]
    print(f'E{i+1} U: {exam_scores}')
    print(f'E{i+1} S: {sorted(exam_scores)}')
    print(f'Class avg: {calculate_average(exam_scores)}%\n')
input('Break!')