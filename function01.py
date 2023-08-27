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
# [Default scores in dictonary]
assignment={1:[12,25],2:[15,30],3:[3,6],4:[50,100]} 
quiz={1:[25,25],2:[30,30],3:[1,6],4:[100,100]}
exam={1:[1,1]}

out_assignment=""   # Print assignment score
out_quiz=""         # Print quiz score
out_exam=""         # Print exam score
r_time=1            # Refresh score when after modify score

clear()
proj_header(version)
print(f"[INFO]")
std_l=input('Last Name: ')
std_f=input('First Name: ')
std_m=input('Mi. Name: ')
#std_l='Buday'
#std_f='Mark Cedie'
#std_m='B'
while True:
    std_id=input('Enter Student ID(ex.: 202289999): ')
    std_id_len=len(std_id)
    if std_id_len==9:
        std_id=int(std_id)
        break
    print(' [!] Your Student id is not valid!')
std_id=202280005
std=std_info(std_l,std_f,std_m,std_id)
while True:
    clear()
    function01_database='function01-data'
    proj_header(version)
    if os.path.exists(f'{function01_database}.txt'):
        pass
        # print(f'Data Loaded: {function01_database}.txt')
    else:
        with open(f'{function01_database}.txt','w') as f:
            f.write('Name=Function 01') #
            f.write('\n\n')
            f.write("assignment=")
            f.write("quiz=")
            f.write("exam=")
            f.close
    
    weight={'assignment':0.2,
              'quiz':0.35,
              'exam':0.45}
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
                elif edit_modifier=='a': # Assignment Grade Editor
                    while True:
                        edit_head=1
                        clear()
                        proj_header(version)
                        print('ASSIGNMENT:')
                        for key,value in assignment.items():
                            print(f'  {edit_head} | {value}')  # n < 4 for stright
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
                            print(f'  {edit_head} | {value}')  # n < 4 for stright
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
                            print(f'  {edit_head} | {value}')  # n < 4 for stright
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

        elif main_modifier=='p': # Process data for student data
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




