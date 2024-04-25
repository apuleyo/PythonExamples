import mysql.connector

#Conexión a la BBDD1
mydb = mysql.connector.connect(
    host="140.0.24.24",
    user="root",
    password="root123"
)

#Conexión a la BBDD2
mydb2 = mysql.connector.connect(
    host="140.0.25.135",
    user="root",
    password="root123"
)

#Fechas de comienzo y fin
begin = "2022-07-22 00:00:00"
end = "2022-07-22 23:59:59"

print("Start:", begin)
print("End:", end)


mycursor = mydb.cursor()

mycursor.execute("SELECT rf.*, count(spsr.recordFiles_id) FROM gemycr.RecordFile rf  \
left join gemycr.SiprecParticipantStreamassoc_recordfile spsr ON spsr.recordFiles_id = rf.id \
  where rf.BeginDate BETWEEN '" + begin + "' AND '" + end + "' group by rf.id")

myresult = mycursor.fetchall()
print("Found ", len(myresult), " results in ", mydb.server_host)

mycursor2 = mydb2.cursor()
mycursor2.execute("SELECT rf.*, count(spsr.recordFiles_id) FROM gemycr.RecordFile rf  \
left join gemycr.SiprecParticipantStreamassoc_recordfile spsr ON spsr.recordFiles_id = rf.id \
  where rf.BeginDate BETWEEN '" + begin + "' AND '" + end + "' group by rf.id")

res = mycursor2.fetchall()
print("Found ", len(res), " results in ", mydb2.server_host)


erract = 0
errnotfound = 0
errmultiple = 0


i = 0


def idfromname(n):
    fileext = n.split('.')
    names = fileext[0].split('-')
    return names[1]+"-"+names[2]


for x in myresult:
    i = i+1
    id = idfromname(x[3])
    # print(x)
    act = x[8]
    myresult2 = list(filter(lambda t: id in t[3], res))
    cnt = len(myresult2)
    if cnt == 1:
        act2 = myresult2[0][8]
        if act != act2:
            print()
            print("ERROR ACT", id, act, act2, x[1])
            erract = erract+1
    else:
        print()
        print("ERROR", id, cnt, x[1])
        if cnt == 0:
            errnotfound = errnotfound+1
        elif cnt > 1:
            errmultiple = errmultiple+1
        for y in myresult2:
            print(y)

print()
print("err=", erract, "notfound=", errnotfound,
      "multiple=", errmultiple, "in", mydb2.server_host)
