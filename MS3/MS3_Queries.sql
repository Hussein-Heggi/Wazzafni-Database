
-- 1) All Job Postings for a given sector
SELECT J.Comp_Name, J.Title, J.Location, J.Date_Posted, J.Vacancies, J.Experience, J.Career_Level, J.Education_Level, J.Min_Salary, J.Max_Salary
FROM Job_Post J INNER JOIN Organizations C 
ON J.Comp_Name = C.Comp_Name INNER JOIN Organizations_Sector S
On C.Comp_Name = S.Comp_Name
WHERE SectorName = ?;

-- 2) All Job Postings for a given set of skills
SELECT J.Comp_Name, J.Title, J.Location, J.Date_Posted, J.Vacancies, J.Experience, J.Career_Level, J.Education_Level, J.Min_Salary, J.Max_Salary
FROM Job_Post J INNER JOIN Requires R
ON J.Title = R.Job_Title AND J.Comp_Name = R.Comp_Name AND J.Location = R.Location
WHERE R.Skill_Name = ? OR R.Skill_Name = ?;

-- 3) Top 5 sectors by number of Job Posts, and the average salary range for each
SELECT DISTINCT (S.Sector), ROUND(AVG(J.Max_Salary - J.Min_Salary),0) AS "Average Salary Range"
FROM Organizations_Sector S INNER JOIN Job_Post J
ON S.Comp_Name = J.Comp_Name
GROUP BY 1
ORDER BY CASE WHEN AVG(J.Max_Salary - J.Min_Salary) IS NOT NULL
THEN COUNT(Title) END DESC
LIMIT 5;

-- 4) Top 5 skills that are in the highest demand
SELECT Skill_Name 
FROM Requires
GROUP BY 1
ORDER BY COUNT(*) DESC
LIMIT 5;

-- 5) Top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date
SELECT C.Comp_Name, C.Location, C.Foundation_Date, C.Min_Size, C.Max_Size, C.URL
FROM Organizations C INNER JOIN Job_Post J
ON C.Comp_Name = J.Comp_Name
WHERE C.Comp_Name != "Confidential Company" AND C.Location LIKE '%Egypt'
ORDER BY CASE WHEN C.Foundation_Date IS NOT NULL 
THEN J.Vacancies/(year(current_date()) - C.Foundation_Date) end DESC
limit 5;

-- 6) Top 5 most paying companies in the field in Egypt
SELECT C.Comp_Name, C.Location, C.Foundation_Date, C.Min_Size, C.Max_Size, C.URL, J.Max_Salary
FROM Organizations C INNER JOIN Job_Post J
ON C.Comp_Name = J.Comp_Name INNER JOIN Under U
ON J.Title = U.Job_Title AND J.Comp_Name = U.Comp_Name AND J.Location = U.Location 
WHERE Category_Name = "IT/Software Development" AND C.Location LIKE '%Egypt' AND C.Comp_Name != "Confidential Company" 
GROUP BY 1,2,3,4,5,6,7
ORDER BY 7 DESC, 1
LIMIT 5;

-- 7) All the postings for a given Organization
SELECT Comp_Name, Title, Location, Date_Posted, Vacancies, Experience, Career_Level, Education_Level, Min_Salary, Max_Salary
FROM Job_Post
WHERE Comp_Name = ? ;

-- 8) Top 5 categories (other than IT/Software Development) under Job Posts
SELECT Category_Name 
FROM Under U
WHERE Category_Name != "IT/Software Development"
GROUP BY 1
ORDER BY COUNT(Job_Title) DESC
LIMIT 5;

-- Validate Email
SELECT Email 
FROM Users; 

-- Validate Skill
SELECT Skill_Name 
FROM Skill;

-- Register a user
INSERT INTO Users (Email, Username, Gender, Birth_Date, GPA) 
VALUES (?,?,?,?,?);

-- Add a new application
INSERT INTO Apply (Comp_Name, Job_Title, Location, User_Email, Application_Date, Cover_Letter) 
VALUES (?,?,?,?,?,?);



