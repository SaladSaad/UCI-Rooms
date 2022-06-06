### This script takes a csv file and loads it into the Course model in the database

import csv, os, sys, django

sys.path.append(os.getcwd()+'/grapher')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rooms.settings')
django.setup()

# TODO: First object key =6 because of header. Set to 0
from grapher.models import Course
 

def load_courses():
    with open('data/parsed-courses.csv', 'r') as file:
        csvFile=csv.reader(file)
        next(csvFile, None)

        for course in csvFile:
            Course.objects.create(code=int(course[0]), days=course[1], starttime=int(course[2]), endtime=int(course[3]), location=course[4])

    
    print(Course.objects.all()) 
    

load_courses()