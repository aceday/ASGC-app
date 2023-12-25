# <202280005@psu.palawan.edu.ph>
# Function 1: Calculate Weighted Average
# Coder1: Mark Cedie Buday @ BSCS2-B1
# Coder2: John Lester Balmaceda @ BSCS2-B1
# Schedule01: T: 11:00-13:00 CE Bldg 15
# Schedule02: F: 10:00-13:00 NIT 1
# Date Created: 2023-08-25
# Added database using sqlite3
import os,time,datetime,sqlite3
from func_backend import *
version=2.2 #### Adding sqlite3 database ####
db="data2.db" # Database name in file
out_ctl=10 # Default for loop
t_std_name='bscs2b1' # Course
t_std_sub='bscs2b1_course'
t_std_mark='bscs2b1_mark' # Students' Markings
output_type = ['assignment', 'quiz', 'exam']
sample_std=(0,'Buday','Marc') # Sample student
ssub=[1, 'ObjOrientedProg',10,10,10] # Sample subject
sout=[0, 'quiz', 1 ,5, 5, 1]
weight=[0.25,0.35,0.4]
if not os.path.isfile(db): # Create default table
    con=sqlite3.connect(db)
    cur=con.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {t_std_name} (
                    std_id INTEGER,
                    last_name TEXT,
                    first_name TEXT
                )""")
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {t_std_sub} (
                    course_id INTEGER,
                    course_name TEXT,
                    assignment_max INTEGER,
                    quiz_max INTEGER,
                    exam_max INTEGER
                )""")
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {t_std_mark} (
                    std_id INTEGER,
                    output_type TEXT,
                    output_no INTEGER,
                    raw_score INTEGER,
                    total_score INTEGER,
                    course_id INTEGER
                )""")
    ## 0, 1, 5, 5
    con.commit() # Save Created Table
    ##### Preinstalled data #####
    cur.execute(f"""INSERT INTO {t_std_name} VALUES ({sample_std[0]},'{sample_std[1]}','{sample_std[2]}')""")
    cur.execute(f"""INSERT INTO {t_std_sub} VALUES ({ssub[0]},'{ssub[1]}',{ssub[2]},{ssub[3]},{ssub[4]})""")
    cur.execute(f"""INSERT INTO {t_std_mark} VALUES ({sout[0]},'{sout[1]}',{sout[2]},{sout[3]},{sout[4]},{sout[5]})""")
    con.commit()
    con.close()
    print('\nDefault table is created')
    time.sleep(3)
else:
    clear()
    print('Database is exist to be loaded!')
    time.sleep(1)
con=sqlite3.connect(db)
cur=con.cursor()
while True:
    clear()
    print(proj_header(version))
    print(f"[{poster('1')}]")
    print("[1] Student System")
    print("[2] Grading System")
    print("[3] Course Editor")
    print("[4] Print Grades")
    
    print("\n[e] Exit")
    main_selection=input("\n:: menu > ")
    # main_selection='2' # Shortcut
    if main_selection=='1':
        while True:
            clear()
            print(proj_header(version))
            print(f"[{poster('12')}]")
            print('[a] Add Student')
            print('[e] Edit Student')
            print('[s] Search Student')
            print('[l] All students')
            print('[d] Delete Student')
            print('\n[m] Main Menu')
            std_menu=input(':: student > ')
            if std_menu=='a':
                clear()
                print(proj_header(version))
                print(f"[{poster('12')}]")
                print('\n>> Add student <<')
                while True: # must 9 digit and integer
                    std_id=input('Student ID: ')
                    std_id_len=len(std_id)
                    if std_id_len==9:
                        std_id=int(std_id)
                        break
                    else:
                        print('Error input!, Student ID must 9-digits')
                std_l=input('Last Name: ')
                std_f=input('First Name: ')
                print('\nAdding...')
                cur.execute(f"""INSERT INTO {t_std_name} VALUES ({std_id}, '{std_l}', '{std_f}')""")
                con.commit()
                print('Done!')
                time.sleep(1)
            elif std_menu=='e': # Use search method to use edit
                while True:
                    clear()
                    print(proj_header(version))
                    print(f"[{poster('12')}]")
                    print('\n>> Edit student <<')
                    print('[i] ID | [a] Check all student lists | [m] Back to student main')
                    std_edit=input(':: search > ').lower()
                    if std_edit=='i': # Use search first and edi
                        while True:
                            clear()
                            print(proj_header(version))
                            print(f"[{poster('12')}]")
                            print('\n>> Edit student <<')
                            while True:
                                try:
                                    std_search_id=int(input('Enter student id to search: '))
                                    break
                                except ValueError:
                                    print('\n  [!] Error input!')
                            cur.execute(f"""SELECT * FROM {t_std_name} WHERE std_id={std_search_id}""")
                            search_id_data=cur.fetchone()
                            if search_id_data is None:
                                print(f'\nStudent ID: {std_search_id} is not found!')
                                time.sleep(2)
                                break
                            else:
                                list_done=search_id_data
                                print(f"\nFound! \n[{poster('61')}]")
                                print(f'ID: {list_done[0]}')
                                print(f'Last Name: {list_done[1]}')
                                print(f'First Name: {list_done[2]}')
                            std_edit_modify=input('\nEdit student data?y/N > ').lower()
                            if std_edit_modify=='y':
                                    while True:
                                        try:
                                            std_edit_id=int(input('Enter new ID: '))
                                            break
                                        except ValueError:
                                            print('\n   [!] Error input!')
                                    std_edit_l=input('Enter last name: ')
                                    std_edit_f=input('Enter first name: ')
                                    cur.execute(f"UPDATE {t_std_name} SET std_id = {std_edit_id}, last_name = '{std_edit_l}', first_name = '{std_edit_f}' WHERE std_id = {list_done[0]}")
                                    con.commit()
                                    out_ctl=0
                                    break
                            else:
                                out_ctl=0
                        if out_ctl==0:
                            break
                    elif std_edit=='a':
                        clear()
                        print(proj_header(version))
                        print(f"[{poster('12')}]")
                        print('\n>> Edit student <<')
                        print('\nLIST OF REGISTERED STUDENTS: \n')
                        cur.execute(f"SELECT * FROM {t_std_name}")
                        std_lists=cur.fetchall()
                        for std in std_lists:
                            print(f'\nID: {std[0]}')
                            print(f'Last Name: {std[1]}')
                            print(f'First Name: {std[2]}')
                        any_key()
                    elif std_edit=='m':
                        break
                        
            elif std_menu=='s': # Search student in 4 methods
                while True:
                    clear()
                    print(proj_header(version))
                    print(f"[{poster('12')}]")
                    print('\n>> Search student <<')
                    print('[i] ID | [l] Last Name | [f] First Name')
                    std_search=input(':: search > ')
                    if std_search=='i':
                        while True:
                            clear()
                            print(proj_header(version))
                            print(f"[{poster('12')}]")
                            print('\n>> Search student <<')
                            while True:
                                try:
                                    std_search_id=int(input('Enter student id to search: '))
                                    break
                                except ValueError:
                                    print('\n  [!] Error input!')
                            cur.execute(f"""SELECT * FROM {t_std_name} WHERE std_id={std_search_id}""")
                            search_id_data=cur.fetchone()
                            if search_id_data is None:
                                print(f'\nStudent ID: {std_search_id} is not found!')
                                any_key()
                            else:
                                list_done=search_id_data
                                print(f"\nFound 1\n[{poster('61')}]")
                                print(f'ID: {list_done[0]}')
                                print(f'Last Name: {list_done[1]}')
                                print(f'First Name: {list_done[2]}')
                                any_key()
                    elif std_search=='l': # Search last name
                        while True:
                            clear()
                            print(proj_header(version))
                            print(f"[{poster('12')}]")
                            print('\n>> Search student <<')
                            std_search_l=input('Enter last name to search: ')
                            cur.execute(f"""SELECT * FROM {t_std_name} WHERE last_name='{std_search_l}'""")
                            search_l_data=cur.fetchall()
                            if search_l_data==[] or None:
                                print(f'\nLast Name {std_search_l} is doesnt exists!')
                                any_key()
                            else:
                                list_done=search_l_data
                                count_done=len(search_l_data)
                                print(f'\nFound {count_done}')
                                for i in list_done:
                                    print(f'ID: {i[0]}')
                                    print(f'Last Name: {i[1]}')
                                    print(f'First Name: {i[2]}\n')
                                any_key()
                    elif std_search=='f': # Search first name
                        while True:
                            clear()
                            print(proj_header(version))
                            print(f"[{poster('12')}]")
                            print('\n>> Search student <<')
                            std_search_f=input('Enter first name to search: ')
                            cur.execute(f"""SELECT * FROM {t_std_name} WHERE first_name='{std_search_f}'""")
                            search_f_data=cur.fetchall()
                            if search_f_data==[] or None:
                                print(f'\nLast Name {std_search_f} is doesnt exists!')
                                any_key()
                            else:
                                list_done=search_f_data
                                count_done=len(search_f_data)
                                print(f'\nFound {count_done}')
                                for i in list_done:
                                    print(f'ID: {i[0]}')
                                    print(f'Last Name: {i[1]}')
                                    print(f'First Name: {i[2]}\n')
                                any_key()
            elif std_menu=='l': # List all registered students
                while True:
                    clear()
                    print(proj_header(version))
                    print(f"[{poster('12')}]")
                    print('\n>> List all students <<\n')
                    print(' STUDENT ID | Name')
                    cur.execute(f"SELECT * FROM {t_std_name}")
                    std_list=cur.fetchall()
                    for std in std_list:
                        print(f"  {std[0]} | {std[1]}, {std[2]}") 
                    any_key()
                    break                                      
            elif std_menu=='d': # Delete student data
                while True:
                    clear()
                    print(proj_header(version))
                    print(f"[{poster('12')}]")
                    print('\n>> Delete student <<')
                    while True:
                        try:
                            std_del_id=input('Enter ID to delete: ')
                            std_del_id_len=len(std_del_id)
                            if std_del_id_len==9:
                                break
                            else:
                                print(f'\n   [!] Must exact 9-digit ID')
                                any_key()
                        except ValueError:
                            print('\n   [!] Invalid error')
                    cur.execute(f"SELECT * FROM {t_std_name} WHERE std_id={std_del_id}") 
                    std_del_found=cur.fetchone()
                    if std_del_found is None:
                        print(f"ID {std_del_id} doesn't exists to delete!")
                    else:
                        print(f'\nID: {std_del_found[0]}')
                        print(f'Last Name: {std_del_found[1]}')
                        print(f'First Name: {std_del_found[2]}')
                        std_del_confirm=input('Confirm to delete? y/N: ').lower()
                        if std_del_confirm=='y':
                            cur.execute(f"DELETE FROM {t_std_name} WHERE std_id={std_del_id}")
                            con.commit()
                            print('\nDeleted Done!')
                            any_key()
                            break
                        else:
                            print('\nDelete Cancelled')
                            any_key()
                            break

            elif std_menu=='m':
                break
    elif main_selection=='2':
        while True:
            clear()
            out_ctl=1
            print(proj_header(version))
            print(f"[{poster('13')}]")
            print('[ag] Add Grade')
            print('[eg] Edit Grade')
            print('[dg] Delete Grade')
            print('\n[m] Main Menu')
            std_menu=input(':: grade > ').lower()
            # std_menu='eg' # Shortcut
            if std_menu=='m':
                break
            elif std_menu=='ag':
                while True:
                    clear()
                    print(proj_header(version))
                    print(f"[{poster('13')}]")
                    print('\n>> Add grade <<')
                    while True:
                        try:
                            std_grade_add_id=input('Enter ID: ')
                            # std_grade_add_id='202280005'
                            std_grade_add_id_len=len(std_grade_add_id)
                            if std_grade_add_id_len==9:
                                std_grade_add_id_int=int(std_grade_add_id)
                                cur.execute(f"SELECT * FROM {t_std_name}")
                                std_info=cur.fetchall()
                                # print(std_info)
                                #print(f'User: {std_grade_add_id}')
                                # print(f'Data: {std_info[0]}')
                                found=0
                                for std in std_info:
                                    # print(f'ID: {std[0]}{type(std[0])}={std_grade_add_id}{type(std_grade_add_id)}')
                                    if std[0]==int(std_grade_add_id_int):
                                        found=1
                                        print('\nFound!') # Return it later
                                        break
                                if found==0:
                                    print(f'\nStudent id {std_grade_add_id} not found\n')
                                    time.sleep(2)
                                else:
                                    break
                            else:
                                print('\n   [!] Must exact 9-digit ID')
                        except ValueError:
                            print('\n   [!] Error input!')
                    cur.execute(f"""SELECT * FROM {t_std_sub}""")
                    sub_data=cur.fetchall()
                    print('\nAvailable subjects: ')
                    print('ID | Subject') # 0 and 5 for id and 5 or more is subject
                    for sub in sub_data:
                        print(f'{sub[0]}  | {sub[1]}')    
                    while True: # Selecting subject
                        
                        try:
                            std_grade_add_sub_data=input('\nEnter subject: ')
                            # print(f'User: {std_grade_add_sub_data}')
                            # print(f'{sub_data}')
                            std_grade_add_sub=int(std_grade_add_sub_data)
                            match=0
                            for sub in sub_data: # 1, OOP, 10, 10, 10
                                # print(f'Subject{sub} / \nCourse ID:{sub[0]}')
                                if sub[0]==std_grade_add_sub:
                                    match=1
                                    subject_add_copy=sub
                                    print('\nPresent!')
                                    sub_pass=sub[0]
                                    break                                        
                                else:
                                    pass
                                    # print('\n   [!] No subject should exists!')
                            if match==1:
                                break
                        except ValueError:
                            pass
                            # print('\n   [!] No subject should exists!')
                            
                    print('\n[a] Assignment | [q] Quiz | [e] Exam')
                    while True:
                        std_grade_course_output_type=input('\n:: Output type: ')
                        if std_grade_course_output_type=='a':
                            out_type=output_type[0] # Output: 'assignment'
                            sub_out=2 # Max Assignment
                            out_type_int=2
                        elif std_grade_course_output_type=='q':
                            out_type=output_type[1] # Output: 'quiz'
                            sub_out=3 # Max Quiz
                            out_type_int=3
                        elif std_grade_course_output_type=='e':
                            out_type=output_type[2] # Output: 'exam'
                            sub_out=4 # Max exam
                            out_type_int=4
                        else:
                            print('\n   [!] Try again!')
                        print(' [0] Exit')
                        while std_grade_course_output_type=='a' or std_grade_course_output_type=='q' or std_grade_course_output_type=='e': # Input output no
                            
                            try:
                                output_no=int(input('Enter output no.: '))
                                    # Checking output no, if exists
                                cur.execute(f"SELECT * FROM {t_std_mark} WHERE std_id={std_grade_add_id_int}")
                                chk_output=cur.fetchall()
                                if chk_output==[]:
                                    out_ctl=3
                                if output_no==0:
                                        out_ctl=0
                                        break
                                out_ctl=3
                                for chk_output_proc in chk_output:
                                    # print(chk_output_proc) 
                                    # print('\n',subject_add_copy)
                                    # print(chk_output_proc)  
                                    if subject_add_copy[0]==chk_output_proc[5]:
                                        #print('Course: ',subject_add_copy[0],'= Course from data',chk_output_proc[5])
                                        #print('Couse ID: ',subject_add_copy[0])
                                        #print('Course_id from Data',chk_output_proc[5])
                                        #print('Output no.:',output_no,'=',chk_output_proc[2])
                                        #print('Output max: ',subject_add_copy[sub_out])
                                        if output_no==chk_output_proc[2] and out_type==chk_output_proc[1]:
                                        # 1. In this condition must      less than output_no less than equal course's max output
                                        # 2. Not equal of output no and output's max output
                                            out_ctl=2
                                            break
                                        elif output_no==chk_output_proc[2] and (output_no>subject_add_copy[sub_out]):
                                            out_ctl=1
                                            break
                                if out_ctl==0:
                                    break
                                elif out_ctl==1:
                                    print(f'Must less than equal {subject_add_copy[sub_out]}')
                                elif out_ctl==2:
                                    print('Same output!')
                                elif out_ctl==3:
                                    # print('Not found')
                                    while True:
                                        try:
                                            add_raw_score=int(input('Enter raw score: '))
                                            add_total_score=int(input('Enter total score: '))
                                            while True:
                                                add_confirm=input(f'Confirm to add {add_raw_score}/{add_total_score} Y/n: ').lower()
                                                if add_confirm=='n':
                                                    out_ctl=0
                                                    break
                                                else:
                                                    clear()
                                                    #print(f'Table: {t_std_mark}')
                                                    #print(f'ID: {std_grade_add_id_int}')
                                                    #print(f'Output type: {output_type}')
                                                    #print(f'Output no.: {output_no}')
                                                    #print(f'Raw score: {add_raw_score}')
                                                    #print(f'Total score: {add_total_score}')
                                                    cur.execute(f"INSERT INTO {t_std_mark} VALUES ({std_grade_add_id_int}, '{out_type}', {output_no}, {add_raw_score}, {add_total_score}, {subject_add_copy[0]})")
                                                    con.commit()
                                                    print('\nAdded done!')
                                                    time.sleep(3)
                                                    another=input('\nAdd another output? y/N: ').lower()
                                                    if another=='y':
                                                        out_ctl=25
                                                        break
                                                    else:
                                                        out_ctl=0
                                                        break
                                            if out_ctl==0:
                                                break
                                        except ValueError:
                                            print('\n   [!] Error input!')
                                        if out_ctl==25:
                                            break
                                if out_ctl==0:
                                    break
                                
                            except ValueError:
                                print('\n   [!] Error input')
                        if out_ctl==0:
                            break
                    if out_ctl==0:
                        break
                if out_ctl==0:
                    break
            c=0
            while std_menu=='eg':
                if out_ctl==0:
                    break
                clear()
                print(proj_header(version))
                print(f"[{poster('13')}]")
                print('\n>> Edit grade <<')
                try:
                    std_grade_edit_id=input('Enter ID: ')
                    std_grade_edit_id_len=len(std_grade_edit_id)
                    while std_grade_edit_id_len==9:
                        found=-1
                        std_grade_edit_id_int=int(std_grade_edit_id)
                        cur.execute(f"SELECT * FROM {t_std_name}")
                        std_info=cur.fetchall()
                        print(std_info)
                        #print(f'[{sample_std}]+1')
                        if std_info==f'[{sample_std}]':
                            print('Sample mode')
                            any_key()
                            found=0
                        if std_info==[] or None:
                            print('No registered ID in this database once!')
                            any_key()
                            found=0
                        for std in std_info:
                            if std[0]==std_grade_edit_id_int:
                                found=1
                                print(f'\n   [OK] ID: {std[0]} Found')
                                time.sleep(0)
                        if found==0:
                            out_ctl=0
                        while found==1:
                            cur.execute(f"SELECT * FROM {t_std_sub}")
                            course_read=cur.fetchall()
                            print('\nAvailable subjects:')
                            print('ID | Subject')
                            for sub in course_read:
                                print(f'{sub[0]}  | {sub[1]}')
                            while True:
                                match=0
                                try:
                                    std_grade_edit_sub_data_int=int(input('\nEnter subject: '))
                                except ValueError:
                                    print('\n   [!] Error input!')
                                    time.sleep(2)
                                std_grade_edit_sub_data=std_grade_edit_sub_data_int
                                for sub in course_read:
                                    if std_grade_edit_sub_data==sub[0]:
                                        match = 1
                                        subject_edit_copy = sub
                                        print('\nPresent!')
                                        sub_pass = sub[0]
                                        break
                                if match==1:
                                    break
                                # print('\n   [!] No subject should exists!')
                            print('OK!')
                            cur.execute(f"SELECT * FROM {t_std_mark} WHERE std_id={std_grade_edit_id_int}")
                            search_output=cur.fetchall()
                            print(f'Student ID: {std_grade_edit_id}')
                            print(f'Name: {std[1]}, {std[2]}\n')

                            print('Format: [output_type] : output_no : Raw/Total ')
                            # filtered_data_ass = [item for item in search_output_ass if item[5] == f'{std_grade_edit_sub_data}']
                            while True: # Display
                                clear()
                                    #Filter output with student's id
                                filtered_out_data = [item for item in search_output if item[5] == std_grade_edit_sub_data]
                                    # Filter with assignment
                                filtered_out_ass = [item for item in search_output if item[1] == 'assignment']
                                filtered_out_quiz = [item for item in search_output if item[1] == 'quiz']
                                filtered_out_exam = [item for item in search_output if item[1] == 'exam']

                                # sorted_data_ass = sorted(filtered_data, key=lambda x: x[2])
                                for out in filtered_out_ass+filtered_out_quiz+filtered_out_exam: # Scan assignment
                                    if out[5]==std_grade_edit_sub_data:
                                        #print(out)
                                        print(f'[{out[1]}] : {out[2]} : {out[3]}/{out[4]}')
                                print('\n [a] assignment [q] quiz [e] Exam [m] [fe] Exit')
                                edit_trig=0
                                edit_trig_inner=0
                                while True:
                                    edit_cur=input(':: edit > ').lower()
                                    if edit_cur=='a':
                                        edit_type=output_type[0]
                                        edit_trig=1
                                    elif edit_cur=='q':
                                        edit_type=output_type[1]
                                        edit_trig=1
                                    elif edit_cur=='e':
                                        edit_type=output_type[2]
                                        edit_trig=1
                                    elif edit_cur=='fe':
                                        out_ctl=0
                                    while edit_trig==1:
                                        print('Ok')
                                        try:
                                            edit_out_where=int(input('Output no.: '))
                                            if edit_cur=='a':
                                                print('Assignment')
                                                for edit_out in filtered_out_ass:
                                                    edit_out_where==edit_out[2]
                                                    edit_trig_inner=2
                                                    # break
                                            elif edit_cur=='q':
                                                print('Quiz')
                                                for edit_out in filtered_out_quiz:
                                                    edit_out_where==edit_out[2]
                                                    edit_trig_inner=2
                                                    # break
                                            elif edit_cur=='e':
                                                print('Exam')
                                                for edit_out in filtered_out_exam:
                                                    edit_out_where==edit_out[2]
                                                    edit_trig_inner=2
                                                    # break
                                            for out in filtered_out_ass+filtered_out_quiz+filtered_out_exam:
                                                if out[5]==std_grade_edit_sub_data and edit_out_where==out[2]:
                                                    print(out)
                                                    break
                                                elif out==[]:
                                                    print('No data')
                                        except ValueError:
                                            print('\n   [!] Error input!')
                                        while edit_trig_inner==2:
                                            # print(out)
                                            try:
                                                std_edit_raw_score=int(input('Enter new raw score: '))
                                                std_edit_total_score=int(input('Enter new total score: '))
                                                edit_confirm=input('Confirm to modify? y/N: ').lower()
                                                if edit_confirm=='y':
                                                    # (202280005, 'assignment', 1, 1, 1, 1)
                                                    # cursor.execute("UPDATE your_table SET column_name = ?", (new_value,))
                                                    # cursor.execute("UPDATE your_table SET column1 = ?, column2 = ?, column3 = ?, column4 = ?, column5 = ?, column6 = ? WHERE entry_id = ?"
                                                    # cur.execute(f"UPDATE {t_std_mark} SET raw_score={std_edit_raw_score}, total_score={std_edit_total_score} WHERE std_id= {std_grade_edit_id_int} AND WHERE output_type='{edit_type}' AND WHERE output_no={edit_out_where}")
                                                    cur.execute(f"UPDATE {t_std_mark} SET raw_score={std_edit_raw_score}, total_score={std_edit_total_score} WHERE std_id={std_grade_edit_id_int} AND output_type='{edit_type}' AND output_no={edit_out_where}")
                                                    con.commit()
                                                    print('Done!')
                                                    time.sleep(1)
                                                    out_ctl=0
                                                    edit_trig=0
                                                    if out_ctl==0:
                                                        break
                                            except ValueError:
                                                print('\n   [!] Error input!')
                                        if out_ctl==0:
                                            break
                                    if out_ctl==0:
                                        break
                                print('\n   [!] Error input!')
                                if out_ctl==0:
                                    break        
                            if out_ctl==0:
                                break
                        if out_ctl==0:
                            break
                    if out_ctl==0:
                        break
                    if out_ctl==0:
                        std_menu==""
                        break            
                except ValueError:
                    print('\n[!]   Error')
                print(f'\n   [!] ID: {std_grade_del_id} not found!')
            while std_menu=='dg' and not out_ctl==0:
                clear()
                print(proj_header(version))
                print(f"[{poster('13')}]")
                print('\n>> Delete grade <<')
                std_grade_del_id=input('Enter ID: ')
                if std_grade_del_id=='0':
                    break
                std_grade_del_id_len=len(std_grade_del_id)
                while std_grade_del_id_len==9:
                    if out_ctl==0:
                        break
                    found=-1
                    std_grade_del_int=int(std_grade_del_id)
                    cur.execute(f"SELECT * FROM {t_std_name}")
                    std_info=cur.fetchall()
                    # print(std_info)
                    
                    for std in std_info:
                        print(std)
                        if std[0]==std_grade_del_int:
                            found=1
                            print(f'\n   [OK]   ID: {std[0]} Found')
                            time.sleep(2)
                    if std_info==f"{sample_std}":
                        print('Sample mode')
                        any_key()
                        found=0
                    elif std_info==[] or None:
                        print('No registered ID in this database once!')
                        any_key()
                        found=0
                    else:
                        if found!=1:
                            found=0
                            print('\n   [!] Not found!')
                            time.sleep(2)
                            break

                    if found==0:
                        out_ctl=0
                    while found==1:
                        if out_ctl==0:
                            break
                        cur.execute(f"SELECT * FROM {t_std_sub}")
                        course_read=cur.fetchall()
                        print('\nAvailable subjects:')
                        print('ID | Subject')
                        for sub in course_read:
                            print(f'{sub[0]}  | {sub[1]}')
                        while True:
                            match=0
                            try:
                                std_grade_del_sub_data_int=int(input('\nEnter subject: '))
                            except ValueError:
                                print('\n   [!] Error input!')
                                time.sleep(2)
                            std_grade_del_sub_data=std_grade_del_sub_data_int
                            for sub in course_read:
                                if std_grade_del_sub_data==sub[0]:
                                    match=1
                                    subject_del_copy=sub
                                    break
                            if match==1:
                                break
                        print('OK!')
                        cur.execute(f"SELECT * FROM {t_std_mark} WHERE std_id={std_grade_del_int}")
                        search_output=cur.fetchall()
                        print(f'Student ID: {std_grade_del_id}')
                        print(f'Name: {std[1]}, {std[2]}')
                        print('Format: [output_type] : output_no : Raw/Total ')
                        while True:
                            found_out=0
                            if out_ctl==0:
                                break
                            out_ctl=1
                            clear()
                            filtered_out_data = [item for item in search_output if item[5] == std_grade_del_sub_data]
                            filtered_out_ass = [item for item in search_output if item[1] == 'assignment']
                            filtered_out_quiz = [item for item in search_output if item[1] == 'quiz']
                            filtered_out_exam = [item for item in search_output if item[1] == 'exam']
                            for out in filtered_out_ass+filtered_out_quiz+filtered_out_exam:
                                if out[5]==std_grade_del_sub_data:
                                    print(f'[{out[1]}] : {out[2]} : {out[3]}/{out[4]}')
                            print('\n [a] assignment [q] quiz [e] Exam [m] [fe] Exit\n')
                            del_trig=0
                            del_trig_inner=0
                            while True:
                                if out_ctl==0:
                                    break
                                del_cur=input(':: delete > ').lower()
                                if del_cur=='a':
                                    del_type=output_type[0]
                                    del_trig=1
                                elif del_cur=='q':
                                    del_type=output_type[1]
                                    del_trig=1
                                elif del_cur=='e':
                                    del_type=output_type[2]
                                    del_trig=1
                                elif del_cur=='fe':
                                    out_ctl=0
                                    break
                                while True:
                                    print('Ok!')
                                    try:    
                                        del_out_where=int(input('Output no.: '))
                                        if del_cur=='a':
                                            print('Assignment')
                                            for del_out in filtered_out_ass:
                                                if del_out_where==del_out[2]:
                                                    del_trig_inner=2
                                                elif del_out_where!=del_out[2]:
                                                    found_out=0
                                        elif del_cur=='q':
                                            print('Quiz')
                                            for del_out in filtered_out_quiz:
                                                if del_out_where==del_out[2]:
                                                    del_trig_inner=2
                                                elif del_out_where!=del_out[2]:
                                                    found_out=0
                                        elif del_cur=='e':
                                            print('Exam')
                                            for del_out in filtered_out_exam:
                                                if del_out_where==del_out[2]:
                                                    del_trig_inner=2
                                                elif del_out_where==del_out[2]:
                                                    found_out=0
                                                        
                                        else:
                                            print('\n   [!] Error input!')
                                        if found_out==0:
                                            print(f'\n   No output recorded')
                                        for out in filtered_out_ass+filtered_out_quiz+filtered_out_exam:
                                            if out[5]==std_grade_del_sub_data:
                                                if del_out_where==out[2]:
                                                    print(out)
                                                    break
                                                elif out==[]:
                                                    print('No data')
                                        while del_trig_inner==2:
                                            del_confirm=input(f'\nDelete?\nOutput: {del_out_where}\nOutput Type: {del_type} @ Course {out[5]}\n::y/N:').lower()
                                            if del_confirm=='y':
                                                cur.execute(f"DELETE FROM {t_std_mark} WHERE std_id={std_grade_del_int} AND output_type='{del_type}' AND output_no={out[2]}")
                                                con.commit()
                                                print('Deleted!')
                                                time.sleep(2)
                                                del_trig_inner=0
                                                out_ctl=0
                                        else:
                                            out_ctl=0
                                            break
                                    except ValueError:
                                        print('\n   [!] Error input!')

    elif main_selection=='3': # Course Editor
        clear()
    elif main_selection=='4': # Print Grades
        clear()
        print(proj_header(version))
        std_id=input('Enter student ID: ')
        #std_id='202280005'
        while len(std_id)==9:
            if out_ctl==0:
                break
            std_id_int=int(std_id)
            cur.execute(f"SELECT * FROM {t_std_name}")
            std_info=cur.fetchall()
            found=0
            for std in std_info:
                if std[0]==std_id_int:
                    found=1
                    print(f'\n   ID: {std_id_int} found!')
                    break
            if found==0:
                print(f'/n   [!] ID: {std_id_int}')
                break
            elif found==1:
                cur.execute(f"SELECT * FROM {t_std_mark} WHERE std_id={std_id_int}")
                list_scores=cur.fetchall()
                assignment=[]
                quiz=[]
                exam=[]
                pa_ass=output_type[0]
                pa_quiz=output_type[1]
                pa_exam=output_type[2]
                for out in list_scores: # Filtering assignment, quiz, exam
                    p_write=0
                    if out[1]==pa_ass:
                        print(f'A: {out}')
                        assignment.append(out)
                    elif out[1]==pa_quiz:
                        print(f'Q: {out}')
                        quiz.append(out)
                    elif out[1]==pa_exam:
                        print(f'E: {out}')
                        exam.append(out)
                std_name=f'{std[1]}, {std[2]}'
                std_id_pr=std_id_int
                std_weight=weight
                display_std(std_name,std_id,std_weight,assignment,quiz,exam)
            break
            # any_key()
        else:
            print('\nMust input 9-digit student id')
    elif main_selection=='e':
        exit()
    out_ctl=10

