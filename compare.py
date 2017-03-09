#Author:Ashley Jiang 2017-03-07
import csv
import sys
import io

file_stream = io.open("/home/ashleyjiang28/Desktop/excel/student employee.csv", mode='r', buffering=-1, encoding=None,
 errors=None, newline=None, closefd=True)
lower_stream = (line.lower() for line in file_stream)
csv_HR = csv.reader(lower_stream, delimiter =',')

fp = open("/home/ashleyjiang28/Desktop/excel/ADlistings2017.csv","r")
csv_AD = (csv.reader(fp, delimiter=',', doublequote = True))
header_AD = csv_AD.next()
#testrow=[row for idx, row in enumerate(csv_AD) if idx == 2]
#print testrow

display_name_AD = header_AD.index("DisplayName")
office_AD = header_AD.index("Office")
title_AD = header_AD.index("Title")


header_HR = csv_HR.next()
lname_HR = header_HR.index("lname")
fname_HR = header_HR.index("fname")
location_HR = header_HR.index("location")
desc_HR = header_HR.index("desc")

for row in csv_AD:
    name_split = (''.join(row[display_name_AD])).split(';')
    #print row
    #we split the name into two items as last name and first name
    office = row[office_AD]
    title = row[title_AD]
    lname = name_split[0]
    try:
        fname = name_split[1]
    except:
        pass
    for row in csv_HR:
        if lname == row[lname_HR]:
            #if fname == row[fname_HR]:
                if office == row[location_HR]:
                    if title == row[desc_HR]:
                        continue
                        # the continue statement goes back to the beginning
                        # of the for loop
        with open("output.csv","wb") as f:
            writer=csv.writer(f)
            writer.writerow(row) #which row is being written here?
            print row

            
