from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime
import Levenshtein
#print fuzz.token_set_ratio("sirhan","sirhan")

import MySQLdb as mdb

db = mdb.connect(host="localhost" , user="root", passwd="pragya", db="test")
cursor = db.cursor()

r=  cursor.execute("select * from nov9 ;") #chenge table name according to your database
#print r
rows = cursor.fetchall()

output=[]
startTime = datetime.now()
for name in range(len(rows)):
    for re in range(name+1,len(rows)):
        if (name != re):
            i = fuzz.token_sort_ratio(rows[name][1],rows[re][1])
            print i
            if (i>=90):
                print "insert value"
                output.append((rows[name][0],rows[re][0]))
                print rows[name][1]+"\t"+rows[re][1]
                #print rows[name][0] , rows[re][0]
valueStr = ""
for i in output:
    valueStr=valueStr+" ("+i[0]+","+i[1]+")"+","
    
 
cursor.execute("INSERT INTO rn9 (id,did) VALUES "+valueStr[:-1]) #chenge table name according to your database

db.commit()
cursor.close()
db.close()
print datetime.now() - startTime
print "done"