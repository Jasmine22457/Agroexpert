import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="123",  # Cambia por tu password real
        dbname="Agroexpert"
    )

def crear_usuario(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuario (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cur.close()
    conn.close()

def verificar_usuario(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM usuario WHERE username=%s AND password=%s AND estado=TRUE", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def guardar_consulta(usuario_id, tipo, parametros, resultado):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO consulta (usuario_id, tipo, parametros, resultado) VALUES (%s, %s, %s, %s)",
                (usuario_id, tipo, parametros, resultado))
    conn.commit()
    cur.close()
    conn.close()
