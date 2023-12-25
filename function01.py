# <202280005@psu.palawan.edu.ph>
# Function 1: Calculate Weighted Average
# Coder1: Mark Cedie Buday @ BSCS2-B1
# Coder2: John Lester Balmaceda @ BSCS2-B1
# Schedule01: T: 11:00-13:00 CE Bldg 15
# Schedule02: F: 10:00-13:00 NIT 1
# Date Created: 2023-08-23
import os,time,datetime
from func_backend import *
version=1.2
assignment={1:[12,25],2:[15,30],3:[3,6],4:[50,100]} 
quiz={1:[25,25],2:[30,30],3:[1,6],4:[100,100]}
exam={1:[1,1]}
out_assignment=""
out_quiz=""
out_exam=""
r_time=1
clear()
proj_header(version)
std_l,std_f,std_m=input('Last Name: '),input('First Name: '),input('Mi. Name: ')
std_id=int(input('Enter Student ID(ex.: 202289999): '))
std=std_info(std_l,std_f,std_m,std_id)
while True:
    clear()
    function01_database='function01-data'
    proj_header(version)
    if os.path.exists(f'{function01_database}.txt'):
        pass
    else:
        with open(f'{function01_database}.txt','w') as f:
            f.write('Name=Function 01\n\nassignment=\nquiz=\nexam=')
            f.close
    weight={'assignment':0.2,'quiz':0.35,'exam':0.45}
    if r_time==1:
        r_time-=1
        out_assignment=post_score(assignment,out_assignment)
        out_quiz=post_score(quiz,out_quiz)
        out_exam=post_score(exam,out_exam)
    elif r_time==2:
        out_assignment=""
        out_quiz=""
        out_exam=""
        out_assignment=post_score(assignment,out_assignment)
        out_quiz=post_score(quiz,out_quiz)
        out_exam=post_score(exam,out_exam)
    else:
        pass
    print(f"[{poster('1')}]")
    print(f'Name {std[3]}\nStudent ID: {std[4]}')
    print(f'Assignment: [{len(assignment)}] = {out_assignment}')
    print(f'Quizzes: [{len(quiz)}] = {out_quiz}')
    print(f'Final Exam: [{len(exam)}] = {out_exam}\n')
    print(f'Weight: A: {px_100(weight["assignment"]):.0f}%, Q: {px_100(weight["quiz"]):.0f}%, E: {px_100(weight["exam"]):.0f}% FIXED VALUE')
    print('Choices: [q] Quit, [e] Edit, [p] Process')
    main_modifier=input(':: Enter choices: ').lower()
    try:
        if main_modifier=='q':
            exit()
        elif main_modifier=='e':
            while True:
                clear()
                proj_header(version)
                print(f"[{poster('2')}]")
                print(f'Name: {std[3]}\nStudent ID: {std[4]}')
                if r_time==1:
                    r_time-=1
                    out_assignment = post_score(assignment,out_assignment)
                    out_quiz = post_score(quiz,out_quiz)
                    out_exam = post_score(exam,out_exam)
                elif r_time==2:
                    out_assignment=""
                    out_quiz=""
                    out_exam=""
                    out_assignment = post_score(assignment,out_assignment)
                    out_quiz = post_score(quiz,out_quiz)
                    out_exam = post_score(exam,out_exam)
                    r_time -= 2
                print(f'Assignment: [{len(assignment)}] = {out_assignment}')
                print(f'Quizzes: [{len(quiz)}] = {out_quiz}')
                print(f'Final Exam: [{len(exam)}] = {out_exam}\n')
                print('Choices: [m] Main Menu, [a] Assignment, [q] Quiz, [e] Final Exam')
                edit_modifier=input(':: Enter choices: ').lower()
                if edit_modifier=='m':
                    break
                elif edit_modifier=='a':
                    while True:
                        edit_head=1
                        clear()
                        proj_header(version)
                        print('ASSIGNMENT:')
                        for key,value in assignment.items():
                            print(f'  {edit_head} | {value}')
                            edit_head+=1
                        print('Choices: [s] Save  [d] Delete entry')
                        print('Format: 10/10 ==> 10,10')
                        edit_assignment=input(":: ").lower()
                        if edit_assignment=='s':
                                r_time+=2
                                break
                        elif edit_assignment=='d':
                            try:
                                e_count=len(assignment)
                                del assignment[e_count]
                            except KeyError:
                                print('No data to be deleted!')
                                time.sleep(2)
                        else:
                            e_write=edit_assignment.split(',')
                            e_count=len(assignment) + 1
                            assignment[e_count]=list(e_write)
                elif edit_modifier=='q':
                    while True:
                        edit_head=1
                        clear()
                        proj_header(version)
                        print('QUIZZES:')
                        for key,value in quiz.items():
                            print(f'  {edit_head} | {value}')
                            edit_head+=1
                        print('Choices: [s] Save [d] Delete entry')
                        print('Format: 10/10 ==> 10,10')
                        edit_quiz=input(":: ").lower()
                        if edit_quiz=='s':
                                r_time+=2
                                break
                        elif edit_quiz=='d':
                            try:
                                e_count=len(quiz)
                                del quiz[e_count]
                            except KeyError:
                                print('No data to be deleted!')
                                time.sleep(2)
                        else:
                            e_write=edit_quiz.split(',')
                            e_count=len(quiz) + 1
                            quiz[e_count]=e_write
                elif edit_modifier=='e':
                    while True:
                        edit_head=1
                        clear()
                        proj_header(version)
                        print('QUIZZES:')
                        for key,value in exam.items():
                            print(f'  {edit_head} | {value}')
                            edit_head+=1
                        print('Choices: [s] Save, [e] Exit without Save, [d] Delete entry')
                        print('Format: 10/10 ==> 10,10')
                        edit_exam=input(":: ").lower()
                        if edit_exam=='s':
                                r_time+=2
                                break
                        elif edit_exam=='d':
                            try:
                                e_count=len(exam)
                                del exam[e_count]
                            except KeyError:
                                print('No data to be deleted!')
                                time.sleep(2)
                        else:
                            e_write=edit_exam.split(',')
                            e_count=len(exam) + 1
                            exam[e_count]=e_write

        elif main_modifier=='p':
            while True:
                clear()
                proj_header(version)
                fwd_std0=std[3]
                display_student(fwd_std0,std_id,weight,assignment,quiz,exam)
              
                print('\n[Y]: Yes  [n] No')
                save_data = input('Want save data Y/n: ').lower()
                if save_data=='n':
                    break
                else:
                    printer(version,fwd_std0,std_id,weight,assignment,quiz,exam)
                    break
                breaker=input('')
    except ValueError:
        c_error=input('Invalid Input!')
def post_score(score_dict, out_str):
    for key, value in score_dict.items():
        out_str += f'{value[0]}/{value[1]} '
    return out_str

def px_100(value):
    return value * 100

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def proj_header(version):
    print(f'Function 01: Calculate Weighted Average (v{version})')

def std_info(last_name, first_name, middle_name, student_id):
    return [last_name, first_name, middle_name, student_id]

def poster(num):
    if num == '1':
        return 'MAIN MENU'
    elif num == '2':
        return 'EDIT MENU'

def display_student(name, student_id, weight, assignment, quiz, exam):
    total_assignment = calculate_total_score(assignment)
    total_quiz = calculate_total_score(quiz)
    total_exam = calculate_total_score(exam)
    weighted_average = calculate_weighted_average(total_assignment, total_quiz, total_exam, weight)
    print(f'Student: {name}')
    print(f'Student ID: {student_id}')
    print(f'Total Assignment Score: {total_assignment}')
    print(f'Total Quiz Score: {total_quiz}')
    print(f'Total Exam Score: {total_exam}')
    print(f'Weighted Average: {weighted_average}')

def calculate_total_score(score_dict):
    total_score = 0
    for key, value in score_dict.items():
        total_score += value[0]
    return total_score

def calculate_weighted_average(assignment_score, quiz_score, exam_score, weight):
    weighted_assignment = assignment_score * weight['assignment']
    weighted_quiz = quiz_score * weight['quiz']
    weighted_exam = exam_score * weight['exam']
    return weighted_assignment + weighted_quiz + weighted_exam

def printer(version, name, student_id, weight, assignment, quiz, exam):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f'{name}_{student_id}_{date}.txt'
    with open(file_name, 'w') as f:
        f.write(f'Function 01: Calculate Weighted Average (v{version})\n')
        f.write(f'Student: {name}\n')
        f.write(f'Student ID: {student_id}\n')
        f.write(f'Weight: A: {px_100(weight["assignment"]):.0f}%, Q: {px_100(weight["quiz"]):.0f}%, E: {px_100(weight["exam"]):.0f}% FIXED VALUE\n')
        f.write(f'Total Assignment Score: {calculate_total_score(assignment)}\n')
        f.write(f'Total Quiz Score: {calculate_total_score(quiz)}\n')
        f.write(f'Total Exam Score: {calculate_total_score(exam)}\n')
        f.write(f'Weighted Average: {calculate_weighted_average(calculate_total_score(assignment), calculate_total_score(quiz), calculate_total_score(exam), weight)}\n')
        f.close()
