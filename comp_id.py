from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime
import Levenshtein
#print fuzz.token_set_ratio("sirhan","sirhan")

import MySQLdb as mdb

db = mdb.connect(host="localhost" , user="root", passwd="pragya", db="test")
cursor = db.cursor()

r=  cursor.execute("select * from companyName ;")
#print r
rows = cursor.fetchall()

#print rows
"""print rows[0][0]
print rows[1][0]"""
startTime = datetime.now()
for name in range(len(rows)):
    #print rows[name]
    #print len(rows)
    for re in range(name+1,len(rows)):
        if (name != re):
            #print rows[name][1]
            i = fuzz.token_set_ratio(rows[name][1],rows[re][1])
            
            #print i
            if (i>=90):
                print "insert value"
                #print "inside if"
        #print list.index(re)
                cursor.execute("""INSERT INTO `repeateName` VALUES (%s,%s) """,(rows[name][0],rows[re][0]))

db.commit()
cursor.close()
db.close()
#print rows[name][0] , rows[re][0]   
print datetime.now() - startTime
print "done"