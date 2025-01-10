# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import itertools
# import random
# import unicodedata
from sqlalchemy import create_engine
# from itertools import islice
# from datetime import date
# from dateutil.relativedelta import relativedelta
import pandas as pd
# import numpy as np
# import re
# import csv




# def Gen_Users():
#     df = pd.DataFrame()
#     num_users = 100
#     unique_usernames = set()
#     Genders = []
#     Emails = []
#     Usernames = []
#
#     while len(unique_usernames) < num_users:
#         username = np.random.choice(
#             ['Ahmed', 'Mohamed', 'Ali', 'Omar', 'Khaled', 'Mahmoud', 'Hassan', 'Amr', 'Youssef', 'Tarek', 'Hesham',
#              'Hany', 'Hussein',
# 'Kareem', 'Yahia', 'Mina', 'Nour', 'Nada', 'Naglaa', 'Nermeen', 'Noha', 'Nahla', 'Nahed', 'Nesma',
#              'Nadine', 'Nabilah',
#              'Nagwa', 'Nahid', 'Najma', 'Najwa', 'Najya', 'Najat', 'Najibah', 'Najeeba', 'Najila', 'Najwa', 'Najat',
#              'Najiyah']) + np.random.choice(
#             ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
#         unique_usernames.add(username)
#     Usernames = list(unique_usernames)
#
#     for i in range(len(Usernames)):
#         if (Usernames[i][0] == 'N'):
#             Genders.append('F')
#
#         else:
#             Genders.append('M')
#
#     for i in range(len(Usernames)):
#         Emails.append(
#             Usernames[i] + np.random.choice(['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@live.com']))
#
#     birthdates = np.random.choice(
#         ['1990-01-01', '1991-01-01', '1992-01-01', '1993-01-01', '1994-01-01', '1995-01-01', '1996-01-01',
#          '1997-01-01', '1998-01-01', '1999-01-01', '2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01',
#          '1980-01-01', '1981-01-01', '1982-01-01', '1983-01-01', '1984-01-01', '1985-01-01', '1986-01-01',
#          '1987-01-01', '1988-01-01', '1989-01-01', '1979-01-01', '1978-01-01', '1977-01-01', '1976-01-01',
#          '1975-01-01', '1974-01-01', '1973-01-01'], size=num_users)
#
#     gpas = np.random.choice(['3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0'],
#                             size=num_users)
#
#     df['Email'] = Emails
#     df['Username'] = Usernames
#     df['Gender'] = Genders
#     df['Birth_Date'] = birthdates
#     df['GPA'] = gpas
#     df.to_csv('Users.csv', index= False)
#
#     Temp = []
#     Skls = []
#     Acquire = []
#
#     SU = pd.read_csv('Skill.csv')
#     SklComp = SU['Skill_Name'].tolist()
#
#     for i in range(len(Emails)):
#         temp = []
#         temp = random.sample(list(SklComp), 4)
#         for j in range(4):
#             Acquirerow = {
#                 'User_Email': Emails[i],
#                 'Skill_Name': temp[j]
#             }
#             Acquire.append(Acquirerow)
#
#     AQ = pd.DataFrame(Acquire)
#     AQ.to_csv('Acquire.csv', index= False)
#
#     JP = pd.read_csv('Job_Post.csv')
#     CompName = JP['Comp_Name'].tolist()
#     JobTitle = JP['Title'].tolist()
#     Loc = JP['Location'].tolist()
#
#     Application_Date = np.random.choice(['2022-01-01', '2023-01-01', '2021-01-01', '2020-01-01', '2019-01-01', '2018-01-01'], size=10)
#     Cover_Letter = "I sing all the time, Please hire me"
#
#     Apply = []
#     for i in range (10):
#         j = random.randint(1, 100)
#         Applyrow = {
#             'Comp_Name': CompName[j],
#             'Job_Title': JobTitle[j],
#             'Location': Loc[j],
#             'User_Email': Emails[i],
#             'Application_Date': Application_Date[i],
#             'Cover_Letter': Cover_Letter
#                    }
#         Apply.append(Applyrow)
#
#     AP = pd.DataFrame(Apply)
#     AP.to_csv('Apply.csv', index=False)
#
# def Get_Links():
#     opts = Options()
#     opts.add_argument('--headless')
#     serv = Service(executable_path="/Users/s7s/Downloads/msedgedriver")
#     driver = webdriver.Edge(service=serv, options=opts)
#     Job_Posts = [0]
#     Companies = [0]
#     i = 0
#     with open("/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Job_Posts_Links.csv", "w", newline="") as Job_Post:
#         with open("/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Companies_Links.csv", "w", newline="") as Company:
#             Jwriter = csv.writer(Job_Post)
#             Cwriter = csv.writer(Company)
#             while (len(Job_Posts) != 0):
#                 Link = "https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?start=" + str(i)
#                 driver.get(Link)
#                 driver.implicitly_wait(5)
#                 Job_Posts = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/h2/a")
#                 Companies = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div/a")
#                 for j in range(len(Job_Posts)):
#                     Jwriter.writerow([Job_Posts[j].get_attribute("href")])
#                     Cwriter.writerow([Companies[j].get_attribute("href")])
#                     print(i, j)
#                 i += 1
#
#     lines = open('/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Companies_Links.csv').read().split('\n')
#     newlines = []
#
#     for line in lines:
#         if (len(line) > 5):
#             if (line[0] == '"'):
#                 line = line[1:len(line)]
#             if line not in newlines:
#                 newlines.append(line)
#
#     Complinks = open('/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Companies_Links.csv', 'w')
#     Complinks.write('\n'.join(newlines))
#     Complinks.close()
#
#     driver.quit()
#
# def Get_Job_Attributes():
#     opts = Options()
#     opts.add_argument('--headless')
#     serv = Service(executable_path="/Users/s7s/Downloads/msedgedriver")
#     driver = webdriver.Edge(service=serv, options=opts)
#
#     JobPost = []
#     JobType = []
#     Require = []
#     Under = []
#     Acquire = []
#     Skill = []
#     Category = []
#
#     CompName = []
#     Adrs = []
#     Tit = []
#     Typs = []
#     Skls = []
#     Catgs = []
#
#     Job_Link = []
#     Comp_Link = []
#
#     with open("/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Job_Posts_Links.csv", "r") as Links:
#         for line in Links:
#             Job_Link.append(line.strip())
#         for x in range(len(Job_Link)):
#             print (x)
#             driver.get(Job_Link[x])
#             driver.implicitly_wait(8)
#             Title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/h1")
#             Types = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/div[1]/a")
#             Address = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/strong[1]")
#             tempp = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/span")
#             if ('Verified' in tempp.text):
#                 Date_Posted = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/span[2]")
#             else:
#                 Date_Posted = tempp
#             Vacancies = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/section[1]/div/div[2]/div/span/span")
#             if (len(Vacancies) != 1):
#                 Vacancies.pop(0)
#             Experience = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[1]/span[2]/span")
#             CareerLevel = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[2]/span[2]/span")
#             EducationLevel = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[3]/span[2]/span")
#             tempo = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[4]/span[2]/span")
#             if ('Male' in tempo.text or 'Female' in tempo.text):
#                 Salary = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[5]/span[2]/span")
#                 Categories = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[6]/ul/li/a/span")
#                 Skills = driver.find_elements(By.XPATH, "html/body/div[1]/div/main/section[2]/div[7]/a")
#             else:
#                 Salary = tempo
#                 Categories = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/section[2]/div[5]/ul/li/a/span")
#                 Skills = driver.find_elements(By.XPATH, "html/body/div[1]/div/main/section[2]/div[6]/a")
#
#             Description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[3]/div").text
#             Description = Description.replace("\n", "").replace("\t", "")
#
#             CompanyText = ''
#             LocationText = ''
#             SkillsText = ''
#             CategoriesText = ''
#             TypesText = ''
#
#             Posted = Date_Posted.text.split(' ')
#             if (Posted[2] == 'minutes' or Posted[2] == 'minute'):
#                 Posted = date.today() - relativedelta(minutes=int(Posted[1]))
#             elif (Posted[2] == 'hours' or Posted[2] == 'hour'):
#                 Posted = date.today() - relativedelta(hours=int(Posted[1]))
#             elif (Posted[2] == 'days' or Posted[2] == 'day'):
#                 Posted = date.today() - relativedelta(days=int(Posted[1]))
#             elif (Posted[2] == 'months' or Posted[2] == 'month'):
#                 Posted = date.today() - relativedelta(months=int(Posted[1]))
#
#             for skill in Skills:
#                 if (len(Skills) > 1):
#                     SkillsText += skill.text + '$'
#                 else:
#                     SkillsText += skill.text
#             if (SkillsText[-1] == '$'):
#                 SkillsText = SkillsText[:len(SkillsText) - 1]
#
#             for category in Categories:
#                 if (len(Categories) > 1):
#                     CategoriesText += category.text + '$'
#                 else:
#                     CategoriesText += category.text
#             if (CategoriesText[-1] == '$'):
#                 CategoriesText = CategoriesText[:len(CategoriesText)-1]
#
#             for type in Types:
#                 if (len(Types) > 1):
#                     TypesText += type.text + '$'
#                 else:
#                     TypesText += type.text
#             if (TypesText[-1] == '$'):
#                 TypesText = TypesText[:len(TypesText)-1]
#
#             Ex1 = Address.text.split("-")
#             if (len(Ex1) == 2):
#                 CompanyText = Ex1[0]
#                 LocationText = Ex1[1]
#             else:
#                 temp1 = "-".join(Address.text.split("-", 2)[:2])
#                 CompanyText = temp1
#                 LocationText = Ex1[2]
#
#             if ('Confidential' in CompanyText):
#                 LocationText = 'Cairo, Egypt'
#
#             Ex2 = Vacancies[0].text.split()
#             Vacancy = int(Ex2[0])
#
#             if ('Confidential' in Salary.text or 'Paid' in Salary.text):
#                 MinSalary = 'NULL'
#                 MaxSalary = 'NULL'
#             else:
#                 Ex3 = Salary.text.split()
#                 if(Ex3[5] == 'Year'):
#                     MaxSalary = int(Ex3[2]/12)
#                     MinSalary = int(Ex3[0]/12)
#                 elif(Ex3[2] == '0'):
#                     MinSalary = None
#                     MaxSalary = None
#                 else:
#                     MaxSalary = int(Ex3[2])
#                     MinSalary = int(Ex3[0])
#
#             CompText = CompanyText.replace("\n", "")
#
#             CompName.append(CompText)
#             Adrs.append(LocationText)
#             Tit.append(Title.text)
#             Typs.append(TypesText)
#             Skls.append(SkillsText)
#             Catgs.append(CategoriesText)
#
#             if ('Not Specified' in Experience.text):
#                 ExpText = 'NULL'
#             else:
#                 ExpText = Experience.text
#
#             if ('Not Specified' in CareerLevel.text):
#                 CarText = 'NULL'
#             else:
#                 CarText = CareerLevel.text
#
#             if ('Not Specified' in EducationLevel.text):
#                 EduText = 'NULL'
#             else:
#                 EduText = EducationLevel.text
#
#             Jobrow = {
#             'Comp_Name': CompText,
#             'Title': Title.text,
#             'Location': LocationText,
#             'Date_Posted': Posted,
#             'Vacancies': Vacancy,
#             'Experience': ExpText,
#             'Career_Level': CarText,
#             'Education_Level': EduText,
#             'Min_Salary': MinSalary,
#             'Max_Salary': MaxSalary,
#             'Job_Description': Description
#                     }
#             JobPost.append(Jobrow)
#     driver.quit()
#
#     for i in range(len(CompName)):
#         if (len(Typs[i].split("$"))>1):
#             temp = Typs[i].split("$")
#             for j in range(len(temp)):
#                 JobTyperow = {
#                 'Comp_Name': CompName[i],
#                 'Title': Tit[i],
#                 'Location': Adrs[i],
#                 'Job_Type': temp[j]
#                 }
#                 JobType.append(JobTyperow)
#         else:
#             JobTyperow = {
#             'Comp_Name': CompName[i],
#             'Title': Tit[i],
#             'Location': Adrs[i],
#             'Job_Type': Typs[i]
#                         }
#             JobType.append(JobTyperow)
#
#     for i in range(len(CompName)):
#         if (len(Skls[i].split("$"))>1):
#             temp = Skls[i].split("$")
#             for j in range(len(temp)):
#                 Requirerow = {
#                 'Comp_Name': CompName[i],
#                 'Job_Title': Tit[i],
#                 'Location': Adrs[i],
#                 'Skill_Name': temp[j]
#                             }
#                 Require.append(Requirerow)
#                 Skillrow = {'Skill_Name': temp[j]}
#                 Skill.append(Skillrow)
#         else:
#             Requirerow = {
#             'Comp_Name': CompName[i],
#             'Job_Title': Tit[i],
#             'Location': Adrs[i],
#             'Skill_Name': Skls[i]
#                         }
#             Require.append(Requirerow)
#             Skillrow = {'Skill_Name': Skls[i]}
#             Skill.append(Skillrow)
#
#     for i in range(len(CompName)):
#         if (len(Catgs[i].split("$"))>1):
#             temp = Catgs[i].split("$")
#             for j in range(len(temp)):
#                 Underrow = {
#                 'Comp_Name': CompName[i],
#                 'Job_Title': Tit[i],
#                 'Location': Adrs[i],
#                 'Category_Name': temp[j]
#                             }
#                 Under.append(Underrow)
#                 Categoryrow = {'Category_Name': temp[j]}
#                 Category.append(Categoryrow)
#         else:
#             Underrow = {
#             'Comp_Name': CompName[i],
#             'Job_Title': Tit[i],
#             'Location': Adrs[i],
#             'Category_Name': Catgs[i]
#                         }
#             Under.append(Underrow)
#             Categoryrow = {'Category_Name': Catgs[i]}
#             Category.append(Categoryrow)
#
#     JP = pd.DataFrame(JobPost)
#     JP = JP.drop_duplicates(subset=['Comp_Name', 'Title', 'Location'])
#     JP.to_csv('Job_Post.csv', index= False)
#
#
#     JT = pd.DataFrame(JobType)
#     JT.drop_duplicates(subset=None, inplace=True)
#     JT.to_csv('Job_Type.csv', index= False)
#
#     RQ = pd.DataFrame(Require)
#     RQ['Skill_Name'] = RQ['Skill_Name'].str.lower()
#     RQ.drop_duplicates(subset=None, inplace=True)
#     RQ.to_csv('Requires.csv', index= False)
#
#     UN = pd.DataFrame(Under)
#     UN.drop_duplicates(subset=None, inplace=True)
#     UN.to_csv('Under.csv', index= False)
#
#     SK = pd.DataFrame(Skill)
#     SK['Skill_Name'] = SK['Skill_Name'].str.lower()
#     SK.drop_duplicates(subset=None, inplace=True)
#     SK.to_csv('Skill.csv', index= False)
#
#     CT = pd.DataFrame(Category)
#     CT['Category_Name'] = CT['Category_Name'].str.lower()
#     CT.drop_duplicates(subset=None, inplace=True)
#     CT.to_csv('Category.csv', index= False)
#
# def Get_Organization_Attributes():
#     opts = Options()
#     opts.add_argument('--headless')
#     serv = Service(executable_path="/Users/s7s/Downloads/msedgedriver")
#     driver = webdriver.Edge(service=serv, options=opts)
#
#     Comp_Link = []
#     Companies = []
#     CompName = []
#     CompSectors = []
#     Sects = []
#
#     with open("/Users/s7s/Desktop/Uni Fall 2023/Database/Project_MS2/Companies_Links.csv", "r") as Links:
#         for line in Links:
#             Comp_Link.append(line.strip())
#         for x in range(len(Comp_Link)):
#             print(x)
#             driver.get(Comp_Link[x])
#             driver.implicitly_wait(4)
#
#             try:
#                 Name = driver.find_element(By.CLASS_NAME, "css-12s37jy").text
#                 Name = Name.replace("Not Verified", "")
#                 Name = Name.replace("Verified", "").replace("New Company", "")
#
#             except:
#                 Name = 'NULL'
#
#             try:
#                 URL = driver.find_element(By.CSS_SELECTOR, "#app>div>div:nth-child(3)>div>div>div.css-12e2e2p>div.css-aqnjlk>div.css-1517rho>a").get_attribute("href")
#             except:
#                 URL = 'NULL'
#
#             try:
#                 Info = driver.find_elements(By.CSS_SELECTOR, "#profile-section > div")
#             except:
#                 Info = None
#
#             try:
#                 see_more = driver.find_element(By.CSS_SELECTOR, "#profile-section > p > span")
#                 if see_more.text:
#                     see_more.click()
#             except:
#                 pass
#
#             try:
#                 Description = driver.find_element(By.CSS_SELECTOR, "#profile-section > p").text
#                 Description = Description.replace("\n", "").replace("\t", "")
#             except:
#                 Description = 'NULL'
#
#             print(Name)
#             CompName.append(Name)
#             InfoText = ''
#             Location = 'NULL'
#             Industry = 'NULL'
#             FoundationDate = 'NULL'
#             SizeText = 'NULL'
#
#             Ex5 = Info[0].text.split("\n")
#             for i in range(len(Ex5)):
#                 if Ex5[i] == "Founded:":
#                     FoundationDate = Ex5[i + 1]
#                 elif Ex5[i] == "Company Size:":
#                     SizeText = Ex5[i + 1]
#                 elif Ex5[i] == "Industry:":
#                     Industry = Ex5[i + 1]
#                 elif Ex5[i] == "Location:":
#                     Location = Ex5[i + 1]
#
#             if (Industry != 'NULL'):
#                 Sects.append(Industry)
#
#             if (SizeText != 'NULL'):
#                 Size = SizeText.split()
#                 if (Size[0] == 'More'):
#                     Min_Size = int(Size[2])
#                     Max_Size = 'NULL'
#                 else:
#                     Ex6 = Size[0].split('-')
#                     Ex7 = Ex6.split();
#                     Min_Size = int(Ex6[0])
#                     Max_Size = int(Ex7[0])
#             else:
#                 Min_Size = 'NULL'
#                 Max_Size = 'NULL'
#             Comprow = {
#                 'Comp_Name': Name,
#                 'Location': Location,
#                 'Foundation_Date': FoundationDate,
#                 'Min_Size': Min_Size,
#                 'Max_Size': Max_Size,
#                 'URL': URL,
#                 'Comp_Description': Description
#                       }
#             Companies.append(Comprow)
#
#     driver.quit()
#
#     CO = pd.DataFrame(Companies)
#     CO.to_csv('Organizations.csv', index= False)
#
#     for i in range(len(Sects)):
#         if (len(Sects[i].split("."))>1):
#             temp = Sects[i].split(".")
#             for j in range(len(temp)):
#                 Sectrow = {
#                 'Comp_Name': CompName[i],
#                 'Sector': temp[j]
#                 }
#                 CompSectors.append(Sectrow)
#         else:
#             Sectrow = {
#             'Comp_Name': CompName[i],
#             'Sector': Sects[i]
#                         }
#             CompSectors.append(Sectrow)
#
#     CS = pd.DataFrame(CompSectors)
#     CS.to_csv('Organizations_Sector.csv', index= False)

from sqlalchemy import create_engine
import pandas as pd
def Populate():
    Names = ["Users", "Organizations", "Organizations_Sector", "Skill", "Category", "Job_Post", "Job_Type", "Apply", "Acquire", "Requires", "Under"]
    CSV = ["Users.csv", "Organizations.csv", "Organizations_Sector.csv", "Skill.csv", "Category.csv", "Job_Post.csv", "Job_Type.csv", "Apply.csv", "Acquire.csv", "Requires.csv", "Under.csv"]
    for i in range(len(CSV)):
        df = pd.read_csv(CSV[i], encoding="utf-8")
        df = df.where(pd.notna(df), None)

    db_user = "root"
    db_password = "Heggi_2002"
    db_host = "localhost"
    db_port = "3306"
    db_name = "Fasa7ni"

    engine_str = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(engine_str)
    table_name = "Predictions"
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    engine.dispose()

Populate()
# Get_Links()
# Get_Job_Attributes()
# Get_Organization_Attributes()
# Gen_Users()












