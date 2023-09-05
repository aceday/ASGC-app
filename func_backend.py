import os,sys,time,datetime,sqlite3
# from function01 import *
# from function01 import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')      
def proj_header(ver):
    x=f':: ASGC-App v.{ver}\n'
    return x
    
def std_info(l,f,m,id):
    mix=f"{l}, {f} {m}"
    mx = []
    for i in l,f,m,mix,id:
        mx.append(i)
    return mx

def any_key():
    akey=input('\nPress any key...')
    
def dbs(db):
    con=sqlite3.connect(db)
    cur=con.cursor()
    if os.path.isfile(db):
        dbf=[]
        for i in con,cur:
            dbf.append(i)
        return dbf 
def percentage(x,y):
    try:
        x=int(x)
        y=int(y)
        z=float(x/y)
    except ZeroDivisionError:
        return 0
    return z

def break_tuple(value):
    return list(value)

def px_100(n):
    return n*100

def grade_rating(value):
    if value <= 100 and value >= 90:
        return 'A'
    elif value <= 89 and value >= 80:
        return 'B'
    elif value <= 79 and value >= 70:
        return 'C'
    elif value <= 69 and value >= 60:
        return 'D'
    elif value <= 59 and value >= 0:
        return 'E'
    else:
        return 'Out of range!'

def weight_final(input, weight):
    return input * weight

def list_str(li):
    a=li[0]
    b=li[1]
    mix=f"{a}/{b}"
    return mix

def poster(n):
    if n=='0':
        return 'None'
    elif n=='01':
        return 'WELCOME'
    elif n=='1':
        return 'MAIN MENU'
    elif n=='11':
        return 'NAME'
    elif n=='12': # Version 2.0
        return 'STUDENT SYSTEM'
    elif n=='13': # Version 2.0
        return 'GRADING SYSTEM'
    elif n=='14': # Version 2.0
        return 'COURSE SYSTEM'
    elif n=='2':
        return 'EDITOR MODE'
    elif n=='3':
        return 'EDIT ASSIGNMENT MODE'
    elif n=='4':
        return 'EDIT QUIZ MODE'
    elif n=='5':
        return 'EDIT EXAM MODE'
    elif n=='51':
        return 'REPORT'
    elif n=='52':
        return 'DATA'
    elif n=='6':
        return 'PROCESS MODE'
    elif n=='61':
        return 'STUDENT DATA'
    elif n=='31':
        return 'ASSIGNMENT'
    elif n=='41':
        return 'QUIZ'
    elif n=='51':
        return 'FINAL EXAM'
    
def post_score(dict_value,out):
    for a, b in dict_value.values():
        mix = f'{a}/{b}, '
        out = out + mix
    return out

def d_text(txt):
    x = ""
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
        x += 'char'
    return x

def datetimenow():
    now = datetime.datetime.now()
    formatted_datetime = now.strftime('%Y%m%d%H%M%S')
    return formatted_datetime

def display_std(name,id,w_dict,a,q,e): # Version 2.0
    clear()
    proj_header('v.2.0')
    print(f"[{poster('61')}]\n")
    print(f'Name: {name}')
    print(f'Student ID: {id}\n')
    #print(f'A: {a}')
    #print(f'Q: {q}')
    #print(f'E: {e}')
    w_ass=w_dict[0]
    w_quiz=w_dict[1]
    w_exam=w_dict[2]
    o_ass_per=0
    o_ass_count=0
    o_quiz_per=0
    o_quiz_conut=0
    o_exam_per=0
    o_exam_count=0
    overall=0
    print('\n:: ASSIGNMENT:')
    for p_out in a:
        raw=p_out[3]
        total=p_out[4]
        print(f"[C{p_out[5]}] : '{p_out[1]}' : {raw}/{total} == {px_100(percentage(raw,total)):.2f}%")
        o_ass_count+=1
        o_ass_per+=percentage(raw,total)
    ow_ass=(o_ass_per/o_ass_count)*w_ass
    print(f'WEIGHTED: A: {px_100(ow_ass)}')
    print('\n:: QUIZ')
    for p_out in q:
        raw=p_out[3]
        total=p_out[4]
        print(f"[C{p_out[5]}] : '{p_out[1]}' : {raw}/{total} == {px_100(percentage(raw,total)):.2f}%")
        o_quiz_conut+=1
        o_quiz_per+=percentage(raw,total)
    ow_quiz=(o_quiz_per/o_quiz_conut)*w_quiz
    print(f'WEIGHTED: Q: {px_100(ow_quiz)}')
    print('\n:: EXAM')
    for p_out in e:
        raw=p_out[3]
        total=p_out[4]
        print(f"[C{p_out[5]}] : '{p_out[1]}' : {raw}/{total} == {px_100(percentage(raw,total)):.2f}%")
        o_exam_count+=1
        o_exam_per+=percentage(raw,total)
    ow_exam=(o_exam_per/o_exam_count)*w_exam
    print(f'WEIGHTED: E: {px_100(ow_exam)}')
    for c in ow_ass,ow_quiz,ow_exam:
        overall+=c
    print(f'\nOVERALL: {px_100(overall):.2f}%')
    print(f'RATING: {grade_rating(px_100(overall))}')
    any_key()
    



def display_student(name,id,w_dict,a,q,e): # Version 1.x without databse
    wa=w_dict["assignment"]
    wq=w_dict["quiz"]
    we=w_dict["exam"]
    print(f"[{poster('61')}]\n")
    print(f'Name: {name}')
    print(f'Student ID: {id}')
    print(f'\n:: ASSIGNMENT:')
    for key,value in a.items():
        print(f"   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%")
    print(f'''Percentage Weighted: {px_100(p_total(a,wq)):.2f}%''')
    print(f'\n:: QUIZ:')
    for key,value in q.items():
        print(f'   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%')
    print(f'''Percentage Weighted: {px_100(p_total(q,wq)):.2f}%''')
    print(f'\n:: EXAM:')
    for key,value in e.items():
        print(f'   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%')
    print(f'''Percentage Weighted: {px_100(p_total(e,we)):.2f}%''')
    ofa=p_total(a,wa)
    ofq=p_total(q,wq)
    ofe=p_total(e,we)
    ovrall=px_100(ofa+ofq+ofe)
    print(f'''\nOVERALL: {ovrall:.2f}%''')
    print(f"Weighted Rating: {grade_rating(ovrall)}")   
def p_total(value,w):
    pt=0
    c=0
    for key,value in value.items():
        m=value[0]
        n=value[1]
        p=percentage(m,n)
        pt+=p
        c+=1
    pt1=pt/c
    pt2=w*pt1
    return pt2

def printer(ver,name,id,w_dict,a,q,e):
    wa=w_dict["assignment"]
    wq=w_dict["quiz"]
    we=w_dict["exam"]
    with open(f'{datetimenow()}-{id}.txt','w') as f:
        f.write(f':: ASGC-App v.{ver}\n\n')
        f.write(f"[{poster('61')}]\n\n")
        f.write(f'Name: {name}\n')
        f.write(f'Student ID: {id}\n')
        f.write(f'\n:: ASSIGNMENT:\n')
        for key,value in a.items():
            f.write(f"   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%\n")
        f.write(f'''Percentage Weighted: {px_100(p_total(a,wq)):.2f}%\n''')
        f.write(f'\n:: QUIZ:\n')
        for key,value in q.items():
            f.write(f'   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%\n')
        f.write(f'''Percentage Weighted: {px_100(p_total(q,wq)):.2f}%\n''')
        f.write(f'\n:: EXAM:\n')
        for key,value in e.items():
            f.write(f'   {key} | {value[0]}/{value[1]} == {px_100(percentage(value[0],value[1])):.2f}%\n')
        f.write(f'''Percentage Weighted: {px_100(p_total(e,we)):.2f}%\n''')
        ofa=p_total(a,wa)
        ofq=p_total(q,wq)
        ofe=p_total(e,we)
        ovrall=px_100(ofa+ofq+ofe)
        f.write(f'''\nOVERALL: {ovrall:.2f}%''')
        f.write(f"\nWeighted Rating: {grade_rating(ovrall)}")