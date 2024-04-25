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
begin = "2024-04-24 00:00:00"
end = "2024-04-25 23:59:59"

print("Start:", begin)
print("End:", end)

mycursor = mydb.cursor()

mycursor.execute("SELECT rf.*, count(spsr.recordFiles_id) FROM gemycr.RecordFile rf  \
left join gemycr.SiprecParticipantStreamassoc_recordfile spsr ON spsr.recordFiles_id = rf.id \
  where rf.BeginDate BETWEEN '" + begin + "' AND '" + end + "' group by rf.id")

#mycursor.execute("SELECT COUNT(*) from gemycr.RecordFile")

myresult = mycursor.fetchall()
print("Found ", len(myresult), " results in ", mydb.server_host)