import sqlite3
import pandas as pd
from IPython.display import display

# Crear conexión a base de datos en memoria (temporal)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Crear tabla y agregar datos
cursor.execute('''
CREATE TABLE personas (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
''')

cursor.executemany('''
INSERT INTO personas (nombre, edad) VALUES (?, ?)
''', [
    ('Ana', 28),
    ('Luis', 35),
    ('Marta', 22),
    ('Carlos', 40)
])

conn.commit()

# Ejecutar consulta
query = 'SELECT * FROM personas WHERE edad > 30'
df = pd.read_sql_query(query, conn)

# Mostrar resultados
display(df)

# Cerrar conexión (opcional)
conn.close()
