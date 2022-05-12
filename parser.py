import requests
from bs4 import BeautifulSoup as bs4
import re
import csv
import pandas as pd


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
    path = 'html/all_depts.html'
    soup = bs4(open(path), 'html.parser')

    data = []
    # data.append(header)
    # for getting the data
    HTML_data = soup.find_all("tr")

    invalid = ['TBA', 'TBATBA']
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

            if((sub_data[3] not in invalid) and (sub_data[2] not in invalid)):
                data.append(sub_data)

    header = ['Code', 'Days', 'Times', 'Location']
    df = pd.DataFrame(data, columns=header)
    df.sort_values(["Location", "Days"], axis=0,
                   ascending=[True, False], inplace=True)
    df.to_csv("parsed-courses.csv", index=False)


if __name__ == "__main__":
    main()
