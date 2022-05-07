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
header = soup.find_all("table")[1].find("tr")
print(header)

data = []
# for getting the data
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

print(data)
print('wubwub')
