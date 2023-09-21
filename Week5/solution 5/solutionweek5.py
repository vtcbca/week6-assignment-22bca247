import csv 
          
#make csv file and insert data
with open('student.csv','w',newline="") as f:
    writer=csv.writer(f)
    header=['sid','sname','city','contact']
    writer.writerow(header)

    rows=[[1,'om','bardoli',99874521020],[2,'sai','Mandvi',8574859652],
          [3,'ram','surat',8745962020],[4,'Radha','bardoli',8963200036],
          [5,'kishan','vyara',7485996621]]
    writer.writerows(rows)

    #insertt user record
    for i in range(5):
        sid=int(input("Enter Student id:"))
        sname=input("Enter Student name:")
        city=input("Enter Student city:")
        contact=input("Enter Student contact:")
        row=[sid,sname,city,contact]
        writer.writerow(row)

#read records from csv file
with open("student.csv",'r',newline="") as f:
    
    read=csv.reader(f)
    head=next(read)
    print("================Students Details==================") 
    print(f"{head[0]}\t{head[1]}\t{head[2]}\t{head[3]}")
    for r in read:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\n")
