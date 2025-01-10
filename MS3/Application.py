import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import dateutil.utils
import re
import os
from tabulate import tabulate
import mysql.connector
from mysql.connector import IntegrityError


conn = mysql.connector.connect(host = "db4free.net", user = "haggog", password = "Heggi_2002", database = "job_finder")

global Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8

Q1 = "SELECT J.Comp_Name, J.Title, J.Location, J.Date_Posted, J.Vacancies, J.Experience, J.Career_Level, J.Education_Level, J.Min_Salary, J.Max_Salary FROM Job_Post J INNER JOIN Organizations C ON J.Comp_Name = C.Comp_Name INNER JOIN Organizations_Sector S On C.Comp_Name = S.Comp_Name WHERE Sector = %s;"
Q2 = "SELECT J.Comp_Name, J.Title, J.Location, J.Date_Posted, J.Vacancies, J.Experience, J.Career_Level, J.Education_Level, J.Min_Salary, J.Max_Salary FROM Job_Post J INNER JOIN Requires R ON J.Title = R.Job_Title AND J.Comp_Name = R.Comp_Name AND J.Location = R.Location WHERE R.Skill_Name = %s;"
Q3 = "SELECT DISTINCT (S.Sector), ROUND(AVG(J.Max_Salary - J.Min_Salary),0) AS 'Average Salary Range' FROM Organizations_Sector S INNER JOIN Job_Post J ON S.Comp_Name = J.Comp_Name GROUP BY 1 ORDER BY CASE WHEN AVG(J.Max_Salary - J.Min_Salary) IS NOT NULL THEN COUNT(Title) END DESC LIMIT 5;"
Q4 = "SELECT Skill_Name FROM Requires GROUP BY 1 ORDER BY COUNT(*) DESC LIMIT 5;"
Q5 = "SELECT C.Comp_Name, C.Location, C.Foundation_Date, C.Min_Size, C.Max_Size, C.URL FROM Organizations C INNER JOIN Job_Post J ON C.Comp_Name = J.Comp_Name WHERE C.Comp_Name != 'Confidential Company' AND C.Location LIKE '%Egypt' ORDER BY CASE WHEN C.Foundation_Date IS NOT NULL  THEN J.Vacancies/(year(current_date()) - C.Foundation_Date) end DESC limit 5;"
Q6 = "SELECT C.Comp_Name, C.Location, C.Foundation_Date, C.Min_Size, C.Max_Size, C.URL, J.Max_Salary FROM Organizations C INNER JOIN Job_Post J ON C.Comp_Name = J.Comp_Name INNER JOIN Under U ON J.Title = U.Job_Title AND J.Comp_Name = U.Comp_Name AND J.Location = U.Location  WHERE Category_Name = 'IT/Software Development' AND C.Location LIKE '%Egypt' AND C.Comp_Name != 'Confidential Company'  GROUP BY 1,2,3,4,5,6,7 ORDER BY 7 DESC, 1 LIMIT 5;"
Q7 = "SELECT Comp_Name, Title, Location, Date_Posted, Vacancies, Experience, Career_Level, Education_Level, Min_Salary, Max_Salary FROM Job_Post WHERE Comp_Name = %s;"
Q8 = "SELECT Category_Name FROM Under U WHERE Category_Name != 'IT/Software Development' GROUP BY 1 ORDER BY COUNT(Job_Title) DESC LIMIT 5;"


def End():
    Menu.destroy()
    Main.destroy()
def is_float(string):
    try:
        round(float(string), 1)
        return True
    except ValueError:
        return False
def Validate_Email():
    Emails = []
    QE = "SELECT Email FROM Users;"
    cursor = conn.cursor()
    cursor.execute(QE,)
    values = cursor.fetchall()
    for x in values:
        for y in x:
            Emails.append(y)
    cursor.close()
    return Emails

def Validate_Skills():
    Skills = []
    QS = "SELECT Skill_Name FROM Skill;"
    cursor = conn.cursor()
    cursor.execute(QS, )
    values = cursor.fetchall()
    for x in values:
        for y in x:
            Skills.append(y)
    cursor.close()
    return Skills

def Validate_Format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def Validate_Date(dob):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, dob))

def Sub1():
    sector = SN.get()

    QS = "SELECT Sector FROM Organizations_Sector WHERE Sector = %s ;"
    cursor = conn.cursor()
    cursor.execute(QS, (sector,))
    value = cursor.fetchall()
    cursor.close()

    if len(value) == 0:
        messagebox.showerror("", "Sector Not Found, Please Try Again")

    else:
        Do1_1.destroy()
        Do1_2 = tk.Toplevel()
        Do1_2.title("Job_Finder")
        Do1_2.geometry("2000x400")

        tree = ttk.Treeview(Do1_2)

        cursor = conn.cursor()
        cursor.execute(Q1, (sector,))
        values = cursor.fetchall()
        cursor.close()

        tree["columns"] = ("name", "title", "location", "date", "vacancy", "experience", "career", "education", "min_salary", "max_salary")

        tree.column("#0", width=0, minwidth=0)
        tree.column("name", width=150, minwidth=150, anchor='center')
        tree.column("title", width=150, minwidth=150, anchor='center')
        tree.column("location", width=150, minwidth=150, anchor='center')
        tree.column("date", width=150, minwidth=150, anchor='center')
        tree.column("vacancy", width=150, minwidth=150, anchor='center')
        tree.column("experience", width=150, minwidth=150, anchor='center')
        tree.column("career", width=150, minwidth=150, anchor='center')
        tree.column("education", width=150, minwidth=150, anchor='center')
        tree.column("min_salary", width=150, minwidth=150, anchor='center')
        tree.column("max_salary", width=150, minwidth=150, anchor='center')


        tree.heading("name", text="Comp_Name", anchor='center')
        tree.heading("title", text="Title", anchor='center')
        tree.heading("location", text="Location", anchor='center')
        tree.heading("date", text="Date_Posted", anchor='center')
        tree.heading("vacancy", text="Vacancies", anchor='center')
        tree.heading("experience", text="Experience", anchor='center')
        tree.heading("career", text="Career_Level", anchor='center')
        tree.heading("education", text="Education_Level", anchor='center')
        tree.heading("min_salary", text="Min_Salary", anchor='center')
        tree.heading("max_salary", text="Max_Salary", anchor='center')


        i = 0
        for j in values:
            tree.insert('', i, text="", values=(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9]))
            i = i + 1

        tree.pack()

def Query1():
    global Do1_1
    Do1_1 = tk.Toplevel()
    Do1_1.title("Job_Finder")
    Do1_1.geometry("800x400")

    label = tk.Label(Do1_1, text="Please Enter the Sector Name", font=('Arial', 20))
    label.pack(pady=50)

    global SN
    SN = tk.Entry(Do1_1, bd=10)
    SN.place(x=300, y=150)

    btn1 = tk.Button(Do1_1, text="Enter", font=('Arial', 22), command=Sub1).place(x=360, y=250)

def Sub2():
    rskills = SKs.get()

    skills = rskills.split(",")

    for skill in skills:
        if skill not in Validate_Skills():
            c = 1
        else:
            c = 0

    if len(rskills) == 0 or c ==1:
        messagebox.showerror("", "Skill Not Found, Please Try Again")

    else:
        Do2_1.destroy()
        Do2_2 = tk.Toplevel()
        Do2_2.title("Job_Finder")
        Do2_2.geometry("2000x400")

        tree = ttk.Treeview(Do2_2)

        tree["columns"] = ("name", "title", "location", "date", "vacancy", "experience", "career", "education", "min_salary", "max_salary")

        tree.column("#0", width=0, minwidth=0)
        tree.column("name", width=150, minwidth=150, anchor='center')
        tree.column("title", width=150, minwidth=150, anchor='center')
        tree.column("location", width=150, minwidth=150, anchor='center')
        tree.column("date", width=150, minwidth=150, anchor='center')
        tree.column("vacancy", width=150, minwidth=150, anchor='center')
        tree.column("experience", width=150, minwidth=150, anchor='center')
        tree.column("career", width=150, minwidth=150, anchor='center')
        tree.column("education", width=150, minwidth=150, anchor='center')
        tree.column("min_salary", width=150, minwidth=150, anchor='center')
        tree.column("max_salary", width=150, minwidth=150, anchor='center')


        tree.heading("name", text="Comp_Name", anchor='center')
        tree.heading("title", text="Title", anchor='center')
        tree.heading("location", text="Location", anchor='center')
        tree.heading("date", text="Date_Posted", anchor='center')
        tree.heading("vacancy", text="Vacancies", anchor='center')
        tree.heading("experience", text="Experience", anchor='center')
        tree.heading("career", text="Career_Level", anchor='center')
        tree.heading("education", text="Education_Level", anchor='center')
        tree.heading("min_salary", text="Min_Salary", anchor='center')
        tree.heading("max_salary", text="Max_Salary", anchor='center')

        cursor = conn.cursor()

        for skill in skills:
            cursor.execute(Q2, (skill,))
            values = cursor.fetchall()
            i = 0
            for j in values:
                tree.insert('', i, text="", values=(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9]))
                i = i + 1

        cursor.close()

        tree.pack()

def Query2():
    global Do2_1
    Do2_1 = tk.Toplevel()
    Do2_1.title("Job_Finder")
    Do2_1.geometry("800x400")

    label = tk.Label(Do2_1, text="Please Enter the Skills as a string separated by commas", font=('Arial', 20))
    label.pack(pady=50)

    global SKs
    SKs = tk.Entry(Do2_1, bd=10)
    SKs.place(x=300, y=150)

    btn2 = tk.Button(Do2_1, text="Enter", font=('Arial', 22), command=Sub2).place(x=360, y=250)

def Query3():
    global Do3
    Do3 = tk.Toplevel()
    Do3.title("Job_Finder")
    Do3.geometry("800x400")
    tree = ttk.Treeview(Do3)

    cursor = conn.cursor()
    cursor.execute(Q3,)
    values = cursor.fetchall()
    cursor.close()

    tree["columns"] = ("sector", "avg salary")

    tree.column("#0", width=0, minwidth=0)
    tree.column("sector", width=250, minwidth=250, anchor='center')
    tree.column("avg salary", width=250, minwidth=250, anchor='center')

    tree.heading("sector", text="Sector", anchor='center')
    tree.heading("avg salary", text="AVG Salary Range", anchor='center')

    i = 0
    for j in values:
        tree.insert('', i, text="", values=(j[0], j[1]))
        i = i+1

    tree.pack()

def Query4():
    global Do4
    Do4 = tk.Toplevel()
    Do4.title("Job_Finder")
    Do4.geometry("800x400")
    tree = ttk.Treeview(Do4)

    cursor = conn.cursor()
    cursor.execute(Q4,)
    values = cursor.fetchall()
    cursor.close()

    tree["columns"] = ("skill")

    tree.column("#0", width=0, minwidth=0)
    tree.column("skill", width=250, minwidth=250, anchor='center')

    tree.heading("skill", text="Skill_Name", anchor='center')

    i = 0
    for j in values:
        tree.insert('', i, text="", values=(j))
        i = i+1

    tree.pack()

def Query5():
    global Do5
    Do5 = tk.Toplevel()
    Do5.title("Job_Finder")
    Do5.geometry("1400x400")
    tree = ttk.Treeview(Do5)

    cursor = conn.cursor()
    cursor.execute(Q5,)
    values = cursor.fetchall()
    cursor.close()

    tree["columns"] = ("name", "location", "date", "min_size", "max_size", "url")

    tree.column("#0", width=0, minwidth=0)
    tree.column("name", width=200, minwidth=200, anchor='center')
    tree.column("location", width=200, minwidth=200, anchor='center')
    tree.column("date", width=200, minwidth=200, anchor='center')
    tree.column("min_size", width=200, minwidth=200, anchor='center')
    tree.column("max_size", width=200, minwidth=200, anchor='center')
    tree.column("url", width=200, minwidth=200, anchor='center')

    tree.heading("name", text="Comp_Name", anchor='center')
    tree.heading("location", text="Location", anchor='center')
    tree.heading("date", text="Foundation_Date", anchor='center')
    tree.heading("min_size", text="Min_Size", anchor='center')
    tree.heading("max_size", text="Max_Size", anchor='center')
    tree.heading("url", text="URL", anchor='center')

    i = 0
    for j in values:
        tree.insert('', i, text="", values=(j[0], j[1], j[2], j[3], j[4], j[5]))
        i = i+1

    tree.pack()

def Query6():
    global Do6
    Do6 = tk.Toplevel()
    Do6.title("Job_Finder")
    Do6.geometry("1400x400")
    tree = ttk.Treeview(Do6)

    cursor = conn.cursor()
    cursor.execute(Q6,)
    values = cursor.fetchall()
    cursor.close()

    tree["columns"] = ("name", "location", "date", "min_size", "max_size", "url")

    tree.column("#0", width=0, minwidth=0)
    tree.column("name", width=200, minwidth=200, anchor='center')
    tree.column("location", width=200, minwidth=200, anchor='center')
    tree.column("date", width=200, minwidth=200, anchor='center')
    tree.column("min_size", width=200, minwidth=200, anchor='center')
    tree.column("max_size", width=200, minwidth=200, anchor='center')
    tree.column("url", width=200, minwidth=200, anchor='center')

    tree.heading("name", text="Comp_Name", anchor='center')
    tree.heading("location", text="Location", anchor='center')
    tree.heading("date", text="Foundation_Date", anchor='center')
    tree.heading("min_size", text="Min_Size", anchor='center')
    tree.heading("max_size", text="Max_Size", anchor='center')
    tree.heading("url", text="URL", anchor='center')

    i = 0
    for j in values:
        tree.insert('', i, text="", values=(j[0], j[1], j[2], j[3], j[4], j[5]))
        i = i+1

    tree.pack()

def Sub7():
    name = CoN.get()

    QC = "SELECT Comp_Name FROM Job_Post WHERE Comp_Name = %s ;"
    cursor = conn.cursor()
    cursor.execute(QC, (name,))
    value = cursor.fetchall()
    cursor.close()

    if len(value) == 0:
        messagebox.showerror("", "Company Not Found, Please Try Again")

    else:
        Do7_1.destroy()
        Do7_2 = tk.Toplevel()
        Do7_2.title("Job_Finder")
        Do7_2.geometry("2000x400")

        tree = ttk.Treeview(Do7_2)

        cursor = conn.cursor()
        cursor.execute(Q7, (name,))
        values = cursor.fetchall()
        cursor.close()

        tree["columns"] = ("name", "title", "location", "date", "vacancy", "experience", "career", "education", "min_salary", "max_salary")

        tree.column("#0", width=0, minwidth=0)
        tree.column("name", width=150, minwidth=150, anchor='center')
        tree.column("title", width=150, minwidth=150, anchor='center')
        tree.column("location", width=150, minwidth=150, anchor='center')
        tree.column("date", width=150, minwidth=150, anchor='center')
        tree.column("vacancy", width=150, minwidth=150, anchor='center')
        tree.column("experience", width=150, minwidth=150, anchor='center')
        tree.column("career", width=150, minwidth=150, anchor='center')
        tree.column("education", width=150, minwidth=150, anchor='center')
        tree.column("min_salary", width=150, minwidth=150, anchor='center')
        tree.column("max_salary", width=150, minwidth=150, anchor='center')


        tree.heading("name", text="Comp_Name", anchor='center')
        tree.heading("title", text="Title", anchor='center')
        tree.heading("location", text="Location", anchor='center')
        tree.heading("date", text="Date_Posted", anchor='center')
        tree.heading("vacancy", text="Vacancies", anchor='center')
        tree.heading("experience", text="Experience", anchor='center')
        tree.heading("career", text="Career_Level", anchor='center')
        tree.heading("education", text="Education_Level", anchor='center')
        tree.heading("min_salary", text="Min_Salary", anchor='center')
        tree.heading("max_salary", text="Max_Salary", anchor='center')


        i = 0
        for j in values:
            tree.insert('', i, text="", values=(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9]))
            i = i + 1

        tree.pack()

def Query7():
    global Do7_1
    Do7_1 = tk.Toplevel()
    Do7_1.title("Job_Finder")
    Do7_1.geometry("800x400")

    label = tk.Label(Do7_1, text="Please Enter the Organization's Name", font=('Arial', 20))
    label.pack(pady=50)

    global CoN
    CoN = tk.Entry(Do7_1, bd=10)
    CoN.place(x=300, y=150)

    btn7 = tk.Button(Do7_1, text="Enter", font=('Arial', 22), command=Sub7).place(x=360, y=250)

def Query8():
    global Do8
    Do8 = tk.Toplevel()
    Do8.title("Job_Finder")
    Do8.geometry("800x400")
    tree = ttk.Treeview(Do8)

    cursor = conn.cursor()
    cursor.execute(Q8,)
    values = cursor.fetchall()
    cursor.close()

    tree["columns"] = ("category")

    tree.column("#0", width=0, minwidth=0)
    tree.column("category", width=250, minwidth=250, anchor='center')

    tree.heading("category", text="Category_Name", anchor='center')

    i = 0
    for j in values:
        tree.insert('', i, text="", values=(j))
        i = i+1

    tree.pack()

def Apply():
    title = JT.get()
    name = CN.get()
    location = JL.get()

    QJ = "Select Comp_Name, Title, Location FROM Job_Post WHERE Comp_Name = %s AND Title = %s AND Location = %s"
    val = (name, title, location)
    cursor = conn.cursor()
    cursor.execute(QJ, val)
    value = cursor.fetchall()
    cursor.close()

    if len(value) == 0:
        messagebox.showerror("", "Job_Post Not Found, Please Try Again")

    else:
        t = 0
        date = datetime.date.today()
        cover = ''
        newval = (name, title, location, email, date, cover)
        cursor = conn.cursor()
        QA = "INSERT INTO Apply (Comp_Name, Job_Title, Location, User_Email, Application_Date, Cover_Letter) VALUES (%s,%s,%s,%s,%s,%s);"
        try:
            cursor.execute(QA, newval)
            conn.commit()
        except IntegrityError as e:
            messagebox.showerror("", "You already applied for this Job Post")
            conn.rollback()
            t = 1

        cursor.close()

        if t != 1:
            messagebox.showinfo("", "Successfully Applied for the Job Post")
            Apply_P.destroy()

def Apply_Page():
    global Apply_P
    Apply_P = tk.Toplevel()
    Apply_P.title("Job_Finder")
    Apply_P.geometry("800x600")

    labelS = tk.Label(Apply_P, text="Application Form", font=('Arial', 24))
    labelS.pack(pady=20)

    label = tk.Label(Apply_P, text="Please Enter the Job Post's Info", font=('Arial', 20))
    label.pack(pady=20)

    global JT, CN, JL

    label1 = tk.Label(Apply_P, text="Title", font=('Arial', 20)).place(x=120, y=203)
    label2 = tk.Label(Apply_P, text="Company", font=('Arial', 20)).place(x=120, y=256)
    label3 = tk.Label(Apply_P, text="Location", font=('Arial', 20)).place(x=120, y=309)

    JT = tk.Entry(Apply_P, bd=10)
    JT.place(x=300, y=200)

    CN = tk.Entry(Apply_P, bd=10)
    CN.place(x=300, y=250)

    JL = tk.Entry(Apply_P, bd=10)
    JL.place(x=300, y=300)

    btnA = tk.Button(Apply_P, text="Enter", font=('Arial',22), command=Apply).place(x=350, y=400)

def Menu():
    global Menu
    Menu = tk.Toplevel()
    Menu.title("Job_Finder")
    Menu.geometry("1200x600")

    label = tk.Label(Menu, text="Welcome, What do you want to do?", font=('Arial', 24))
    label.pack(pady=20)

    button_f = tk.Frame(Menu)

    button_f.columnconfigure(0, weight=1)

    btn1 = tk.Button(button_f, text="All Job Postings for a given sector", font=('Arial', 22), command=Query1)
    btn2 = tk.Button(button_f, text="All Job Postings for a given set of skills", font=('Arial', 22), command=Query2)
    btn3 = tk.Button(button_f, text="Top 5 sectors by number of Job Posts, and the average salary range for each", font=('Arial', 22), command=Query3)
    btn4 = tk.Button(button_f, text="Top 5 skills that are in the highest demand", font=('Arial', 22), command=Query4)
    btn5 = tk.Button(button_f, text="Top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date", font=('Arial', 22), command=Query5)
    btn6 = tk.Button(button_f, text="Top 5 most paying companies in the field in Egypt", font=('Arial', 22), command=Query6)
    btn7 = tk.Button(button_f, text="All the postings for a given Organization", font=('Arial', 22), command=Query7)
    btn8 = tk.Button(button_f, text="Top 5 categories (other than IT/Software Development) under Job Posts", font=('Arial', 22), command=Query8)
    btn9 = tk.Button(button_f, text="Apply For a Job",font=('Arial', 22), command=Apply_Page)
    btn10 = tk.Button(button_f, text="Exit", font=('Arial', 22), command=End)

    btn1.grid(row=0, column=0, sticky="news")
    btn2.grid(row=1, column=0, sticky="news")
    btn3.grid(row=2, column=0, sticky="news")
    btn4.grid(row=3, column=0, sticky="news")
    btn5.grid(row=4, column=0, sticky="news")
    btn6.grid(row=5, column=0, sticky="news")
    btn7.grid(row=6, column=0, sticky="news")
    btn8.grid(row=7, column=0, sticky="news")
    btn9.grid(row=8, column=0, sticky="news")
    btn10.grid(row=9, column=0, sticky="news")

    button_f.pack(pady=70)

def Sign_In():
    global email
    email = input.get()
    if email not in Validate_Email():
        messagebox.showerror("", "Email Not Found, Please Try Again")
    else:
        Signin.destroy()
        Menu()

def Sign_Up():
    email = UE.get()
    name = UN.get()
    gender = UG.get()
    birth = UB.get()
    rgpa =  UGP.get()
    rskills = US.get()


    skills = rskills.split(",")

    for skill in skills:
        if skill not in Validate_Skills():
            c = 1
        else:
            c = 0

    gender.upper()
    gpa = round(float(rgpa), 1)

    if email in Validate_Email() or Validate_Format(email) == False or len(email)>50:
        messagebox.showerror("", "Email Not Eligible, Please Try Again")

    elif Validate_Date(birth) == False:
        messagebox.showerror("", "Date Isn't in the correct form: 'YYYY-MM-DD', Please Try Again")

    elif gender != 'M' and gender != 'F':
        messagebox.showerror("", "Gender Isn't in the correct form: 'M or F', Please Try Again")

    elif is_float(rgpa) == False or gpa < 0.0 or gpa > 4.00:
        messagebox.showerror("", "Invalid GPA, Please Try Again")

    elif c == 1:
        messagebox.showerror("", "Invalid Skill, Please Try Again")

    else:
        cursor = conn.cursor()
        QI = "INSERT INTO Users (Email, Username, Gender, Birth_Date, GPA) VALUES (%s,%s,%s,%s,%s);"
        QR = "INSERT INTO Acquire (User_Email, Skill_Name) VALUES (%s,%s);"
        val = (email, name, gender, birth, gpa)
        cursor.execute(QI, val)
        conn.commit()

        for skill in skills:
            val2 = (email,skill)
            cursor.execute(QR, val2)
            conn.commit()

        cursor.close()
        messagebox.showinfo("", "Successfully Signed Up")
        Signup.destroy()
        Menu()

def Sign_In_Page():
    Main.geometry("0x0")

    global Signin
    Signin = tk.Toplevel()
    Signin.title("Job_Finder")
    Signin.geometry("800x400")

    label = tk.Label(Signin, text="Sign in Page", font=('Arial', 24))
    label.pack(pady=20)

    label = tk.Label(Signin, text="Please Enter Your Email", font=('Arial', 24))
    label.pack(pady=50)

    global input
    input = tk.Entry(Signin, bd=10)
    input.place(x=300,y=200)

    btnl = tk.Button(Signin, text="Enter", font=('Arial', 22), command=Sign_In)
    btnl.pack(pady=50)

def Sign_Up_Page():
    Main.geometry("0x0")

    global Signup
    Signup = tk.Toplevel()
    Signup.title("Job_Finder")
    Signup.geometry("800x600")

    labelS = tk.Label(Signup, text="Sign Up Page", font=('Arial', 24))
    labelS.pack(pady=20)

    labelS2 = tk.Label(Signup, text="Please Enter Your Info", font=('Arial', 20))
    labelS2.pack(pady=20)

    global UE, UN, UG, UB, UGP, US

    label1 = tk.Label(Signup, text="Email", font=('Arial', 20)).place(x=120,y=203)
    label2 = tk.Label(Signup, text="Username", font=('Arial', 20)).place(x=120,y=256)
    label3 = tk.Label(Signup, text="Gender", font=('Arial', 20)).place(x=120,y=309)
    label4 = tk.Label(Signup, text="Birth_Date", font=('Arial', 20)).place(x=120,y=362)
    label5 = tk.Label(Signup, text="GPA", font=('Arial', 20)).place(x=120,y=415)
    label6 = tk.Label(Signup, text="Skills", font=('Arial', 20)).place(x=120, y=468)

    UE = tk.Entry(Signup, bd=10)
    UE.place(x=300, y=200)

    UN = tk.Entry(Signup, bd=10)
    UN.place(x=300, y=250)

    UG = tk.Entry(Signup, bd=10)
    UG.place(x=300, y=300)

    UB = tk.Entry(Signup, bd=10)
    UB.place(x=300, y=350)

    UGP = tk.Entry(Signup, bd=10)
    UGP.place(x=300, y=400)

    US = tk.Entry(Signup, bd=10)
    US.place(x=300, y=450)

    btnS = tk.Button(Signup, text="Enter", font=('Arial', 22), command=Sign_Up).place(x=340,y=520)


def Start():
    global Main
    Main = tk.Tk()
    Main.title("Job_Finder")
    Main.geometry("600x400")

    label = tk.Label(Main, text = "Main Page", font = ('Arial', 24))
    label.pack(pady = 20)

    button_frame = tk.Frame(Main)

    button_frame.columnconfigure(0, weight=1)

    btn1 = tk.Button(button_frame, text="Sign in", font=('Arial', 22), command=Sign_In_Page)
    btn2 = tk.Button(button_frame, text="Sign up", font=('Arial', 22), command=Sign_Up_Page)

    btn1.grid(row = 0, column = 0, sticky = "news")
    btn2.grid(row = 1, column = 0, sticky = "news")

    button_frame.pack(pady=100)
    Main.mainloop()

Start()


