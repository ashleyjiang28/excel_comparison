
#Finished by Ashley Jiang
#03-10-2017
#Credit to Geisel Library IT Operation Unit at University of California-San Diego 
import csv
import sys
import io
import string

def readHRFile():
    file_stream = io.open("/home/ashleyjiang28/Desktop/excel/IT staff list HR.csv", mode='r', buffering=-1, encoding=None,
    errors=None, newline=None, closefd=True)
    lower_stream = (line.lower() for line in file_stream)
    csv_HR = csv.reader(lower_stream, delimiter =',')
    return csv_HR

def readADFile():
    file_stream_AD = io.open("/home/ashleyjiang28/Desktop/excel/ADlistings2017.csv", mode='r', buffering=-1, encoding=None,
    errors=None, newline=None, closefd=True)
    lower_stream_AD = (line.lower() for line in file_stream_AD)
    csv_AD = csv.reader(lower_stream_AD, delimiter =',')
    return csv_AD

header_AD = readADFile().next()

display_name_AD = header_AD.index("displayname")
office_AD = header_AD.index("office")
title_AD = header_AD.index("title")


header_HR = readHRFile().next()
lname_HR = header_HR.index("lname")
fname_HR = header_HR.index("fname")
location_HR = header_HR.index("location")
desc_HR = header_HR.index("desc")

i =0
a = 0
for row in readADFile():
    #we split the name into two items as last name and first name
    office = row[3]
    title = row[10]
    lname = row[1]
    try:
        fname = row[2]
    except:
        fname = 0

    manager_id = row[4].replace("cn=",'')
    for row in readADFile():
        if row[0] == manager_id:
            manager_lname = row[1]

    for row in readHRFile():
        if lname == row[lname_HR]:
            try:
                if fname.strip() == row[fname_HR].strip():
                    if office.strip() == row[location_HR]:
                        split_name = ''.join(row[5]).split(";")
                        if manager_lname == split_name[0]:
                            i = i +1
                            print i
                            print row
                            break
            except:
                pass
                        #continue
                        # the continue statement goes back to the beginning
                        # of the for loop
        
     
        with open("output.csv","wb") as f:
            writer=csv.writer(f)
            writer.writerow(row) #which row is being written here?
    
