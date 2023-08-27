import os,sys,time,datetime
# from function01 import *
# from function01 import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')      
def proj_header(ver):
    print(f':: ASGC-App v.{ver}\n')
def std_info(l,f,m,id):
    mix=f"{l}, {f} {m}"
    mx = []
    for i in l,f,m,mix,id:
        mx.append(i)
    return mx
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
    elif n=='11':
        return 'NAME'
    elif n=='1':
        return 'MAIN MENU'
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
def display_student(name,id,w_dict,a,q,e):
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