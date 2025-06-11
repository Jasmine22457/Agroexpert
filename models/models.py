

import psycopg2
import bcrypt
import secrets
import string
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )

def crear_usuario(username, email, password):
    conn = get_connection()
    cur = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    # Generar código de verificación (6 dígitos)
    verification_code = ''.join(secrets.choice(string.digits) for _ in range(6))
    cur.execute("""
        INSERT INTO usuario (username, email, password, estado, verification_code) 
        VALUES (%s, %s, %s, FALSE, %s)
        RETURNING id
    """, (username, email, hashed_password, verification_code))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id, verification_code

def verificar_usuario(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, password, username, estado 
        FROM usuario 
        WHERE email = %s
    """, (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return (user[0], user[2], user[3])  # id, username, estado
    return None


def verificar_codigo(email, codigo):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE usuario 
        SET estado = TRUE 
        WHERE email = %s AND verification_code = %s
        RETURNING id, username
    """, (email, codigo))
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result

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
    cur.execute("""
        INSERT INTO consulta (usuario_id, tipo, parametros, resultado) 
        VALUES (%s, %s, %s, %s)
    """, (usuario_id, tipo, parametros, resultado))
    conn.commit()
    cur.close()
    conn.close()