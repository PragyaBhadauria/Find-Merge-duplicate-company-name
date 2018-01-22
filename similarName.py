from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime
import Levenshtein
#print fuzz.token_set_ratio("sirhan","sirhan")

import MySQLdb as mdb

db = mdb.connect(host="localhost" , user="root", passwd="pragya", db="test")
cursor = db.cursor()

r=  cursor.execute("select * from company;")
#print r
rows = cursor.fetchall()
g =rows
#print g

csv = open("companyname1.csv", "w") 
columnTitleRow = "name,similarName \n"
csv.write(columnTitleRow)

"""name = "(p&g)"
print name[1:len(name-1)]"""

"""for name in rows:
    print str(name)
    i = process.extract(str(name),g, limit = 3 )
    print i"""

"""query = "p&g"
choices = ('p&g','p&g india Limited','mohan mechem P&g')
l= process.extract(query,choices)
print l"""
startTime = datetime.now()
for name in rows:
    #print name
    for re in rows:
        print rows[0]
        if (name != re):
            i = fuzz.token_set_ratio(name,re)
        #print i
            if (i>=95):
                name = str(name)
                
                name= name[1:len(name)-1]
                #print name
                re = str(re)
                
                re = re[1:len(re)-1]
                #print re
                result = name + "," + re+"\n"
                csv.write(result)
                
                #print name, re
                
print datetime.now() - startTime