from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime
import Levenshtein
#print fuzz.token_set_ratio("sirhan","sirhan")

import MySQLdb as mdb

db = mdb.connect(host="localhost" , user="root", passwd="pragya", db="test")
cursor = db.cursor()

r=  cursor.execute("select * from nov10 ;")
#print r
rows = cursor.fetchall()

#print rows
"""print rows[0][0]
print rows[1][0]"""
a = "abpenterprises"
startTime = datetime.now()
for name in range(len(rows)):
    i = fuzz.ratio(a,rows[name][1])
    #print i
    if (i>=70):
        print i
        print "insert value"
                #print "inside if"
        #print list.index(re)
                #cursor.execute("""INSERT INTO `repeateName` VALUES (%s,%s) """,(rows[name][0],rows[re][0]))
                #print rows[name][0] , rows[re][0]   
print datetime.now() - startTime
print "done"