import pyodbc

server = 'DESKTOP-IO41DBS' # Reemplace la dirección IP con la suya
database = 'demoBD' # Reemplace el nombre de la base de datos con la suya
username = 'sa' # Reemplace el nombre de usuario con el suyo si es necesario
password = 'Dev23.-.*' # Reemplace la contraseña con la suya si es necesario

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    print("Conexión exitosa.")
    
    # Ejecutar una consulta SQL
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
except pyodbc.Error as e:
    print("Error al conectarse al servidor:", e)
    
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
