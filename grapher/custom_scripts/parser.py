import requests
from bs4 import BeautifulSoup as bs4
import re
import csv
import pandas as pd
from datetime import datetime, time


def class_code(class_string):
    return int(class_string)


# TODO: make times() work for double times and add locations capability as well for double locations


# get rid of funky characters, spaces, and then split into days and times
def days_times(ogString):

    if('TBA' in ogString):
        return ('TBA', 'TBA', 'TBA')
    ogString = ogString.replace(u'\xa0', u'')
    ogString = re.sub(" +", " ", ogString)  # getting rid of multiple spaces
    # unicodedata.normalize("NFKD", ogString)
    days, times = ogString.split(' ', 1)

    times = times.replace(' ', '')
    times = re.sub(r'p', 'PM', times)
    times = re.sub(r' ', '0', times)
    start, end = times.split('-', 1)

    start_hour = start.split(':', 1)[0]

    if ('PM' not in end):  # start AM, end AM
        end += 'AM'
    end = datetime.strptime(end, '%I:%M%p')

    # Figure out whether start time is AM or PM
    temp_start_am = start_hour+'AM'
    temp_start_am = datetime.strptime(temp_start_am, '%I%p')

    temp_start_pm = start_hour+'PM'
    temp_start_pm = datetime.strptime(temp_start_pm, '%I%p')

    temp_am_diff = end - temp_start_am
    temp_pm_diff = end - temp_start_pm

    if(temp_am_diff > temp_pm_diff and temp_pm_diff.days > -1):
        start += 'PM'
    else:
        start += 'AM'
    start = datetime.strptime(start, '%I:%M%p')
    start = start.time().strftime('%H%M')
    end = end.time().strftime('%H%M')

    #print('returning: ', days, times)
    return(days, start, end)


def main():
    path = './static/eecs.html'
    soup = bs4(open(path), 'html.parser')

    data = []
    # data.append(header)
    # for getting the data
    HTML_data = soup.find_all("tr")

    invalid = ['TBA', 'TBATBA', 'ON LINE']
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
                    # TODO: FIGURE OUT HOW TO DEAL WITH DOUBLES
                    # THIS CHECK IS A TEMP FIX.
                    if(len(sub_elem_data) < 20):
                        day_time = days_times(sub_elem_data)
                        print(day_time)
                        sub_data.append(day_time[0])  # days
                        sub_data.append(day_time[1])  # start time
                        sub_data.append(day_time[2])  # end time
                    else:
                        sub_data.append('TBA')
                        sub_data.append('TBA')
                        sub_data.append('TBA')
                elif i == 6:  # location
                    sub_data.append(sub_elem_data)
                i += 1

            # check day and location
            if((sub_data[1] not in invalid) and (sub_data[4] not in invalid)):
                data.append(sub_data)

    header = ['Code', 'Days', 'Start_Time', 'End_Time', 'Location']
    df = pd.DataFrame(data, columns=header)
    df.sort_values(["Location", "Start_Time"], axis=0,
                   ascending=[True, True], inplace=True)
    df.to_csv("./static/parsed-courses.csv", index=False)


if __name__ == "__main__":
    #days_times('TuTh    9:30-10:50')
    main()
