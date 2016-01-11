import MySQLdb
import traceback
def updatePhone():
    conn= MySQLdb.connect(host='localhost',port = 3306,user='root',db ='wool')
    cur=conn.cursor()
    filehandle=open('phone2.txt','r')
    for phoneNum in filehandle:
        print "insert into database=====",phoneNum
        try:
            cur.execute("insert into phone(tel) VALUES(%s)",phoneNum)
        except Exception as e:
            print(traceback.print_exc())
    #close the database and commit date
    conn.commit()
    conn.close()
    cur.close()

if __name__ == "__main__":
    updatePhone()
