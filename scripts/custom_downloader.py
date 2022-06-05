### This script downloads all department htmls and appends them to one big html file for parser.py
## Make sure to check all paths before running this script

import requests
from bs4 import BeautifulSoup as bs4



# gets home page of class schedule to get all dept names
# to individually parse later
def depts():
    url = "https://www.reg.uci.edu/perl/WebSoc"
    path = 'data/home.html'
    response = requests.post(url, stream=True)
    with open(path, 'w') as file:
        file.write(response.text)

    soup = bs4(open(path), 'html.parser')

    items = soup.select('[name=Dept] option[value]')
    values = [item.get('value') for item in items]
    del values[0]
    i = 0
    for item in values:
        values[i] = item.replace(" ", "+")
        i += 1
    return values

# gets list of department names, parses each page and saves to file.


def main_Downloader():
    dept_names = depts()

    f = open('data/all_depts.html', 'w')  # clear file init
    f.close()

    url = "https://www.reg.uci.edu/perl/WebSoc"
    for name in dept_names:
        body = f"""Submit=Display+Web+Results&YearTerm=2022-92&Breadth=ANY&Dept={name}&CourseNum=&Division=ANY&CourseCodes=&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Exclude&Bldg=&Room="""
        response = requests.post(url, body, stream=True)
        with open("static/all_depts.html", 'a') as file:
            file.write(response.text)


if __name__ == '__main_Downloader__':
    main_Downloader()
