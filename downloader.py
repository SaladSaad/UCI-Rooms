import requests


def main():
    body = "Submit=Display+Web+Results&YearTerm=2022-92&Breadth=ANY&Dept=EECS&CourseNum=&Division=ANY&CourseCodes=&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Exclude&Bldg=&Room="

    url = "https://www.reg.uci.edu/perl/WebSoc"
    response = requests.post(url, body, stream=True)
    with open("webp.html", 'w') as file:
        file.write(response.text)


if __name__ == '__main__':
    main()
