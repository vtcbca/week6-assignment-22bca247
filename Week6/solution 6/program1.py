import sqlite3 as sq
import csv

con=sq.connect("result.db")
cur=con.cursor()

#1. create table
cur.execute("""create table if not exists stud(
            student_id primary key,
            student_name text,
            sub1 number,
            sub2 number,
            sub3 number,
            sub4 number,
            sub5 number
);""")

#2. insert 10  data in table 
# cur.execute("""insert into stud values
#             (1,"om",90,85,80,78,88),
#             (2,"sai",88,70,56,90,65),
#             (3,"ram",74,70,77,75,60),
#             (4,"radha",56,60,45,70,55),
#             (5,"kishan",80,88,86,87,80),
#             (6,"vijay",60,66,65,45,40),
#             (7,"ajay",77,78,74,75,72),
#             (8,"vikas",50,56,54,25,20),
#             (9,"rahul",35,30,50,20,19),
#             (10,"parth",50,85,90,60,30)
# """)

con.commit()



# 3. dump into csv file using cmd
'''
F:\github\week6>sqlite3 result.db
SQLite version 3.42.0 2023-05-16 12:36:15
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .mode csv
sqlite> .output stude_result.csv
sqlite> select * from stud;
sqlite> .quit
'''

# 4.read csv file and add 2 columns
rows=[]
with open("stude_result.csv","r",newline="") as file:
    reader=csv.DictReader(file)
    rows=list(reader)
    print(rows)

for row in rows:
    total_marks=sum(int(row[f"sub{i}"]) for i in range(1,6))
    percentage=total_marks/5
    if percentage>=90:
        grade='A'
    elif percentage >=80:
        grade='B'
    elif percentage >=70:
        grade='C'
    elif percentage >=60:
        grade='D'
    elif percentage >= 50:
        grade='E'
    else:
        grade='F'

    row['total_marks']=total_marks
    row['grade']=grade

# add column in csv 
with open('stude_result.csv','w',newline="") as file:
    fieldnames=["student_id","student_name","sub1","sub2","sub3","sub4","sub5","total_marks","grade"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# 5.list out top 3

sort_rows=sorted(rows,key=lambda x:x['total_marks'],reverse=True)
print("Top 3 students ")
for i in range(3):
    stud_id=sort_rows[i]['student_id']
    stud_name=sort_rows[i]['student_name']
    total_=sort_rows[i]['total_marks']
    percentage=total_/5
    print(f"student {i+1}")
    print(f"Student_id:{stud_id}\nstudent_name:{stud_name}\ntotal_marks:{total_}\npercentage:{percentage}")
con.close()