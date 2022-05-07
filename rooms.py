import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
import unicodedata
import re
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


def class_code(class_string):
    print(int(class_string))
    return int(class_string)


# TODO: make times() work for double times and add locations capability as well for double locations


# get rid of funky characters, spaces, and then split into days and times
def times(ogString):

    unicodedata.normalize(
        "NFKD", ogString)
    ogString = ogString.replace(" ", "")
    temp = re.compile("([a-zA-Z]+)([0-9:-]+)")
    return list(temp.match(ogString).groups())


def main():
    path = 'webp.html'
    soup = bs4(open(path), 'html.parser')
    with open("webp1.html", 'w') as file:
        file.write(str(soup))

    data = []
    # for getting the data
    HTML_data = soup.find_all("tr")

    for element in HTML_data:
        i = 0
        sub_data = []
        start = (element.get_text()[1:6])
        if(start.isdigit()):
            for sub_element in element:
                sub_elem_data = sub_element.get_text()
                print('i value: ', i)
                if i == 0:
                    print('sub data:', sub_elem_data)
                    sub_data.append(class_code(sub_elem_data))
                elif i == 5:
                    print('sub_data', sub_elem_data)
                    day_time = times(sub_elem_data)
                    sub_data.append(day_time[0])
                    sub_data.append(day_time[1])
                elif i == 6:
                    sub_data.append(sub_elem_data)
                else:
                    print('else data: ', sub_elem_data)
                i += 1

            if(sub_data[2] != 'TBA'):
                data.append(sub_data)

    for classes in data:

        print('bruh')


if __name__ == "__main__":
    main()
"""
            if(sub_data[0].isdigit()):
                print('Class found: ', int(sub_data[0]))
                break
            else:
                break


            if (element[0].isdigit()):
        print('Class found:', int(element[0]))"""
