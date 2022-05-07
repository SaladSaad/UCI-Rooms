import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

"""
body = "Submit=Display+Web+Results&YearTerm=2022-92&Breadth=ANY&Dept=EECS&CourseNum=&Division=ANY&CourseCodes=&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Exclude&Bldg=&Room="

url = "https://www.reg.uci.edu/perl/WebSoc"
response = requests.post(url, body, stream=True)
with open("webp.html", 'w') as file:
    file.write(response.text)


data1 = pd.read_html("webp.html", match='Instructor', skiprows=2)
print(data1)

data1.to_csv('classes.csv')
 """


path = 'webp.html'
soup = bs4(open(path), 'html.parser')
with open("webp1.html", 'w') as file:
    file.write(str(soup))

data = []
# for getting the data
HTML_data = soup.find_all("tr")

rows = [0, 5, 6]
for element in HTML_data:
    i = 0
    sub_data = []
    start = (element.get_text()[0:5])
    if(start.isdigit()):
        for sub_element in element:
            if(i in rows):
                sub_data.append(sub_element.get_text())
            i = i+1

        if(sub_data[2] != 'TBA'):
            data.append(sub_data)

for classes in data:
    print(classes)


""" 
            if(sub_data[0].isdigit()):
                print('Class found: ', int(sub_data[0]))
                break
            else:
                break 
            
            
            if (element[0].isdigit()):
        print('Class found:', int(element[0]))"""
