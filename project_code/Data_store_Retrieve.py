from tkinter import *
import tkinter as tk
import mysql.connector

#************Enter your mysql databse connection**************************************

connection=mysql.connector.connect(host='localhost',user='root',password='berlin',database='student')
mycursor=connection.cursor()

#The save_data function is used as a callback for the save_sql function when the Submit button is clicked."
def save_data():
      save_sql(f_name,l_name,age,email,college,degree,course,mobile)
#The retrieve_data function is used as a callback for the retrieve_sql function when the Retrieve button is clicked."
def retrieve_data():
      retrieve_sql(numb)

#The retrieve_sql function retrieves data from MySQL database when the Retrieve button is clicked
def retrieve_sql(numb):
      numbers=numb.get()
      number=int(numbers)
      query=f"""select * from student_details where Mobile_number = {number} """
      f_name.delete(0,len(f_name.get()))
      l_name.delete(0,len(l_name.get()))
      age.delete(0,len(age.get()))
      email.delete(0,len(email.get()))
      college.delete(0,len(college.get()))
      degree.delete(0,len(degree.get()))
      course.delete(0,len(course.get()))
      mobile.delete(0,len(mobile.get()))

            
      try:
            mycursor.execute(query)
            result=mycursor.fetchall()
            f_name.insert(0,result[0][0])
            l_name.insert(0,result[0][1])
            age.insert(0,result[0][2])
            email.insert(0,result[0][3])
            college.insert(0,result[0][4])
            degree.insert(0,result[0][5])
            course.insert(0,result[0][6])
            mobile.insert(0,result[0][7])
            retlab=Label(master=window, text='one data found',font=lab_font,background='black',foreground='white')
            retlab.grid(column=1,row=13,sticky='nw')
      except  :
            retlab1=Label(master=window, text='NO data found',font=lab_font,background='black',foreground='white')
            retlab1.grid(column=1,row=13,sticky='nw') 
          
      
#The save_sql function stores data in a MySQL database when the submit button is clicked  
def save_sql(f_names,l_names,ages,emails,colleges,degrees,courses,mobiles):
    if   len(mobiles.get())==10 and (mobiles.get())[0] in ['6','7','8','9'] and mobiles.get().isnumeric() and 17<=int(ages.get())<=30 and emails.get().find('@gmail.com')!=-1:
                                                 
                f_name=f_names.get()
                l_name=l_names.get()
                age=ages.get()
                email=emails.get()
                college=colleges.get()
                degree=degrees.get()
                course=courses.get()
                mobile=mobiles.get()
               
             
                mycursor.execute("show tables like 'student_details'")
                batch=mycursor.fetchall()
                if len(batch)==0:
                    query1="""create table student_details(First_name varchar(255),Last_name varchar(255),
                             Age int,Email varchar(255),College_name varchar(255),
                             Degree varchar(255),Course varchar(255),Mobile_number varchar(255) primary key
                                   )"""
                    mycursor.execute(query1)
                
                query2=f"""insert into student_details(First_name,Last_name,Age,Email,College_name,Degree,Course,Mobile_number) values(
                        '{f_name}','{l_name}',{age},'{email}','{college}','{degree}','{course}','{mobile}' 
                            )""" 
                query3=f"""update student_details set First_name='{f_name}',Last_name='{l_name}',
                        Age={age},Email='{email}',College_name='{college}',Degree='{degree}',Course='{course}' 
                          where Mobile_number='{mobile}' """
                try:
                     mycursor.execute(query2)
                     connection.commit()
                     elselab=Label(master=window,text="      Thank you for submitting     ",font=lab_font,background='black',foreground='white')
                     elselab.grid(column=2,row=10,sticky='nw')

                except Exception as e:
                 
                     mycursor.execute(query3)
                     connection.commit()
                     elselab=Label(master=window,text="   you have updated your details    ",font=lab_font,background='black',foreground='white' )
                     elselab.grid(column=2,row=10,sticky='nw')

    else:
          elselab=Label(master=window,text="please enter proper details",font=lab_font)
          elselab.grid(column=2,row=10,sticky='nw')

#------------------------------------------------------------------------------------------------------------------------
window= Tk()
window.title('form')
window.columnconfigure(list(range(18)),minsize=50)
window.rowconfigure(list(range(18)),minsize=50)
lab_font=("Helvetica", 18)
lab_main=Label(master=window,text='Data Storing and Retrieval System',font=("cambria", 30),background='yellow',foreground='blue')
lab_title=Label(master=window,text='Student Details Form:',font=("cambria", 23),background='skyblue')
lab_1=Label(master=window,text="First name",font=("Helvetica", 18))
lab_1a=Label(master=window,text="Last name",font=("Helvetica", 18))
lab_2=Label(master=window,text="Student age",font=("Helvetica", 18))
lab_3=Label(master=window,text="Gmail",font=("Helvetica", 18))
lab_4=Label(master=window,text="College Name",font=("Helvetica", 18))
lab_5=Label(master=window,text="Degree",font=("Helvetica", 18))
lab_5a=Label(master=window,text="Course",font=("Helvetica", 18))
lab_6=Label(master=window,text="Mobile number",font=("Helvetica", 18))
text_font=("cambria", 16)

f_name=Entry(master=window,borderwidth=10,font=("cambria", 16))
l_name=Entry(master=window,borderwidth=10,font=("cambria", 16))
age=Entry(master=window,borderwidth=10,font=("cambria", 16))
email=Entry(master=window,borderwidth=10,font=("cambria", 16))
college=Entry(master=window,borderwidth=10,font=("cambria", 16))
degree=Entry(master=window,borderwidth=10,font=("cambria", 16))
course=Entry(master=window,borderwidth=10,font=("cambria", 16))
mobile=Entry(master=window,borderwidth=10,font=("cambria", 16))


lab_main.grid(column=2,row=0,sticky='nw')
lab_title.grid(column=0,row=1,sticky='n')
lab_1.grid(column=0,row=2,sticky='nw')
lab_1a.grid(column=0,row=3,sticky='nw')
lab_2.grid(column=0,row=4,sticky='nw')
lab_3.grid(column=0,row=5,sticky='nw')
lab_4.grid(column=0,row=6,sticky='nw')
lab_5.grid(column=0,row=7,sticky='nw')
lab_5a.grid(column=0,row=8,sticky='nw')
lab_6.grid(column=0,row=9,sticky='nw')



f_name.grid(column=1,row=2,sticky='nw')
l_name.grid(column=1,row=3,sticky='nw')
age.grid(column=1,row=4,sticky='nw')
email.grid(column=1,row=5,sticky='nw')
college.grid(column=1,row=6,sticky='nw')
degree.grid(column=1,row=7,sticky='nw')
course.grid(column=1,row=8,sticky='nw')
mobile.grid(column=1,row=9,sticky='nw')

save_button=Button(master=window,text='Submit',font=("cambria", 20),command= save_data)
save_button.grid(column=0,row=10)

lab_title1=Label(master=window,text='Retrieve data:',font=("cambria", 20),height=2,background='skyblue')
labnum=Label(master=window,text='Enter your mobile number',font=lab_font)
numb=Entry(master=window,font=text_font,borderwidth=10)
ret_button=Button(master=window,text='Retrieve',font=lab_font,command=retrieve_data)

lab_title1.grid(column=0,row=11,sticky='nw')
labnum.grid(column=0,row=12,sticky='nw')
numb.grid(column=1,row=12,sticky='nw')
ret_button.grid(column=0,row=13,sticky='nw')

window.mainloop()

