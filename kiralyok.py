from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='127.0.0.1',
                                 database='kiralyok')
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)


cursor.execute("""
    SELECT uralkodo.nev, hivatal.mettol, hivatal.meddig
        FROM uralkodo
    JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
    JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon
    WHERE uralkodohaz.nev = 'Árpád-ház'
    ORDER BY hivatal.mettol;""")
    
for i in cursor:
    
    print(f"{i}")

cnx.close()