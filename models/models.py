import psycopg2
import bcrypt  

def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="123",  # Cambia por tu password real
        dbname="Agroexpert"
    )

def crear_usuario(username, email, password):
    conn = get_connection()
    cur = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # 👈 Importante
    cur.execute("INSERT INTO usuario (username, email, password, estado) VALUES (%s, %s, %s, TRUE)",
                (username, email, hashed_password))
    conn.commit()
    cur.close()
    conn.close()

def verificar_usuario(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, password, username FROM usuario WHERE email = %s AND estado = TRUE", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return (user[0], user[2])  # id y username
    return None

def correo_existe(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM usuario WHERE email = %s", (email,))
    existe = cur.fetchone() is not None
    cur.close()
    conn.close()
    return existe

def guardar_consulta(usuario_id, tipo, parametros, resultado):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO consulta (usuario_id, tipo, parametros, resultado) VALUES (%s, %s, %s, %s)",
                (usuario_id, tipo, parametros, resultado))
    conn.commit()
    cur.close()
    conn.close()



