import os,sqlite3#mysql_breaker
class System:
    def __name__(self):
        pass
    def clear(self):
        if os.name=='nt':
            os.system('cls') # For Windows NT
        else:
            os.system('clear') # For Linux and Mac OSX
sys0=System()
sys0.clear()
def sl(list)->float:
    l=len(list)
    return sum(list)/l
#con=sqlite3.connect('data2.db')
#cur=con.cursor()
#cur.execute("SELECT * FROM bscs2b1_mark")
#out_list=cur.fetchall()
#for i in out_list:
#    print(i)
std1_ass=[50, 60, 70, 80, 90, 95, 75]
std1_quiz=[80, 75, 88, 92, 90]
std1_exam=[94]

std2_ass=[45, 99, 100, 100, 88, 75, 95]
std2_quiz=[100, 100, 99, 100, 98]
std2_exam=[94]

std3_ass=[46, 76, 88, 98, 97, 91 ,94]
std3_quiz=[81, 82, 83, 84, 85]
std3_exam=[84]

std4_ass=[67, 71, 85, 86, 92, 61, 72]
std4_quiz=[82, 84, 86, 88, 90]
std4_exam=[98]

std5_ass=[50, 74, 87, 92, 94, 96, 100]
std5_quiz=[83, 87, 92, 80, 60]
std5_exam=[82]

a1=[std1_ass[0],std2_ass[0],std3_ass[0],std4_ass[0],std5_ass[0]]
print(f'A1 U: {a1}\nA1 S: {sorted(a1):}')
print(f'Class avg: {sl(a1)}%\n')
a2=[std1_ass[1],std2_ass[1],std3_ass[1],std4_ass[1],std5_ass[1]]
print(f'A2 U: {a2}\nA2 S: {sorted(a2)}')
print(f'Class avg: {sl(a2)}%\n')
a3=[std1_ass[2],std2_ass[2],std3_ass[2],std4_ass[2],std5_ass[2]]
print(f'A3 U: {a3}\nA3 S: {sorted(a3)}')
print(f'Class avg: {sl(a3)}%\n')
a4=[std1_ass[3],std2_ass[3],std3_ass[3],std4_ass[3],std5_ass[3]]
print(f'A4 U: {a1}\nA4 S: {sorted(a1)}')
print(f'Class avg: {sl(a4)}%\n')
a5=[std1_ass[4],std2_ass[4],std3_ass[4],std4_ass[4],std5_ass[4]]
print(f'A5 U: {a5}\nA5 S: {sorted(a5)}')
print(f'Class avg: {sl(a5)}%\n')
a6=[std1_ass[5],std2_ass[5],std3_ass[5],std4_ass[5],std5_ass[5]]
print(f'A6 U: {a6}\nA6 S: {sorted(a6)}')
print(f'Class avg: {sl(a6)}%\n')
a7=[std1_ass[6],std2_ass[6],std3_ass[6],std4_ass[6],std5_ass[6]]
print(f'A7 U: {a7}\nA7 S: {sorted(a7)}')
print(f'Class avg: {sl(a7)}%\n')
q1=[std1_quiz[0],std2_quiz[0],std3_quiz[0],std4_quiz[0],std5_quiz[0]]
print(f'Q1 U: {q1}\nQ1 S: {sorted(q1)}')
print(f'Class avg: {sl(q1)}%\n')
q2=[std1_quiz[1],std2_quiz[1],std3_quiz[1],std4_quiz[1],std5_quiz[1]]
print(f'Q2 U: {q2}\nQ2 S: {sorted(q2)}')
print(f'Class avg: {sl(q2)}%\n')
q3=[std1_quiz[2],std2_quiz[2],std3_quiz[2],std4_quiz[2],std5_quiz[2]]
print(f'Q3 U: {q3}\nQ3 S: {sorted(q3)}')
print(f'Class avg: {sl(q3)}%\n')
q4=[std1_quiz[3],std2_quiz[3],std3_quiz[3],std4_quiz[3],std5_quiz[3]]
print(f'Q4 U: {q4}\nQ4 S: {sorted(q4)}')
print(f'Class avg: {sl(q4)}%\n')
q5=[std1_quiz[4],std2_quiz[4],std3_quiz[4],std4_quiz[4],std5_quiz[4]]
print(f'Q5 U: {q5}\nQ5 S: {sorted(q5)}')
print(f'Class avg: {sl(q5)}%\n')
e1=[std1_exam[0],std2_exam[0],std3_exam[0],std4_exam[0],std5_exam[0]]
print(f'E1 U: {e1}\nE11 S: {sorted()}')
print(f'Class avg: {sl(e1)}%\n')
any=input('Break!')

