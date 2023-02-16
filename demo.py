import psycopg2

# Conexion a la base de datos
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

cur = conn.cursor()

# Query de la database 
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

if not len(rows):
    print("No hay datos")
else:
    for row in rows:
        print(row)

# Cerrando la comunicacion con la base de datos.
cur.close()
conn.close()