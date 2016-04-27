import re


with open('./taf_for_noaa_20160421.txt','r') as taf_messy:
#   with open("tidy_taf.txt','r+') as tidy_taf:
    data = taf_messy.read()
    tidy_taf = open("tidy_taf.txt",'r+')
    for row in data:
        #Check for any non alphanumeric characters and replace with whitespace if non-alphanumeric encountered.
        clean_row = re.sub('[^a-zA-Z0-9\s]',' ',row)
        clean_row = re.sub('^[0-9]{3}',' ',row)
        tidy_taf.write(clean_row)
            

