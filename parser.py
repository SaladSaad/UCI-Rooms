import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
import unicodedata
import re


def class_code(class_string):
    return int(class_string)


# TODO: make times() work for double times and add locations capability as well for double locations


# get rid of funky characters, spaces, and then split into days and times
def times(ogString):
    ogString = ogString.replace(u'\xa0', u'')
    ogString = re.sub(" +", " ", ogString)
    # unicodedata.normalize("NFKD", ogString)
    return(ogString.split(' ', 1))


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
        start = (element.get_text()[0:5])
        if(start.isdigit()):
            for sub_element in element:
                sub_elem_data = sub_element.get_text()
                if i == 0:  # course code
                    sub_data.append(class_code(sub_elem_data))
                elif i == 5:  # day times
                    day_time = times(sub_elem_data)
                    sub_data.append(day_time[0])
                    sub_data.append(day_time[1])
                elif i == 6:  # location
                    sub_data.append(sub_elem_data)
                i += 1

            if(sub_data[3] != 'TBA'):
                data.append(sub_data)

    for classes in data:
        print(classes)


if __name__ == "__main__":
    main()
