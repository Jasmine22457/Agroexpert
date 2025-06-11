from flask import Blueprint, render_template, request, redirect, session, url_for, flash, jsonify
from models.models import crear_usuario, verificar_usuario, guardar_consulta, correo_existe, verificar_codigo, get_connection
from motor_inferencia.motor_inferencia import AsesorAgricola
from base_conocimiento.base_conomiento_plagas import obtener_sintomas_por_cultivo
from werkzeug.security import check_password_hash
from utils import nocache
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import jsonify
from models.models import get_connection
import secrets
import string





asesor = AsesorAgricola()

main_blueprint = Blueprint('main', __name__)

# Configuración del correo (debes poner tus propios datos)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
       'email': 'sistemaagroexpert@gmail.com',
    'password': 'eumb irmj ivkf vvtl'  # Usa contraseña de aplicación para Gmail
}

def enviar_correo_verificacion(destinatario, codigo):
    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL_CONFIG['email']
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Verificación de correo - AgroExpert'
    
    cuerpo = f"""
    <h2>Gracias por registrarte en AgroExpert</h2>
    <p>Tu código de verificación es: <strong>{codigo}</strong></p>
    <p>Ingresa este código en la página de verificación para activar tu cuenta.</p>
    <p>Si no solicitaste este registro, puedes ignorar este mensaje.</p>
    """
    
    mensaje.attach(MIMEText(cuerpo, 'html'))
    
    try:
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
            server.send_message(mensaje)
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False

@main_blueprint.route('/')
@nocache
def index():
    if 'usuario_id' in session:
        return redirect(url_for('main.home'))
    return render_template('login.html')

@main_blueprint.route('/login', methods=['POST'])
@nocache
def login():
    email = request.form['email']
    password = request.form['password']

    user = verificar_usuario(email, password)

    if user:
        if not user[2]:  # Si no está verificado
            return render_template('login.html', error="Por favor verifica tu correo electrónico primero.")
        
        session['usuario_id'] = user[0]
        session['username'] = user[1]
        return redirect(url_for('main.home'))

    return render_template('login.html', error="Usuario no registrado o contraseña incorrecta.")

@main_blueprint.route('/register', methods=['GET', 'POST'])
@nocache
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if correo_existe(email):
            return render_template('register.html', error="El correo ya está registrado.")

        user_id, verification_code = crear_usuario(username, email, password)
        
        # Enviar correo de verificación
        if enviar_correo_verificacion(email, verification_code):
            return redirect(url_for('main.verificar', email=email))
        else:
            return render_template('register.html', error="Error al enviar el correo de verificación. Intenta nuevamente.")
    
    return render_template('register.html')

@main_blueprint.route('/verificar', methods=['GET', 'POST'])
@nocache
def verificar():
    email = request.args.get('email', '')
    
    if request.method == 'POST':
        email = request.form['email']
        codigo = request.form['codigo']
        
        resultado = verificar_codigo(email, codigo)
        if resultado:
            session['usuario_id'] = resultado[0]
            session['username'] = resultado[1]
            return redirect(url_for('main.home'))
        else:
            return render_template('verificar.html', email=email, error="Código incorrecto o expirado")
    
    return render_template('verificar.html', email=email)

# ... (el resto de tus rutas existentes permanecen igual)
@main_blueprint.route('/reenviar-codigo', methods=['POST'])
@nocache
def reenviar_codigo():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'success': False, 'message': 'Email requerido'}), 400
    
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        # Generar nuevo código
        new_code = ''.join(secrets.choice(string.digits) for _ in range(6))
        
        # Actualizar en la base de datos
        cur.execute("""
            UPDATE usuario 
            SET verification_code = %s 
            WHERE email = %s
            RETURNING username
        """, (new_code, email))
        
        if cur.fetchone():
            conn.commit()
            # Enviar el nuevo código
            if enviar_correo_verificacion(email, new_code):
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'message': 'Error al enviar correo'}), 500
        else:
            return jsonify({'success': False, 'message': 'Email no encontrado'}), 404
            
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        cur.close()
        conn.close()
@main_blueprint.route('/logout')
@nocache
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@main_blueprint.route('/home')
@nocache
def home():
    if 'usuario_id' not in session:
        return redirect(url_for('main.index'))
    return render_template('home.html', username=session['username'])

@main_blueprint.route('/fertilizante', methods=['GET', 'POST'])
@nocache
def fertilizante():
    resultado = None
    advertencias = []
    sugerencias = []
    cultivos = asesor.obtener_opciones('cultivos')
    suelos = asesor.obtener_opciones('suelos')
    climas = asesor.obtener_opciones('climas')
    etapas = asesor.obtener_opciones('etapas')
    variedades_dict = asesor.obtener_opciones('variedades_cultivo')
    variedades = []

    if request.method == 'POST':
        cultivo = request.form['cultivo']
        suelo = request.form['suelo']
        clima = request.form['clima']
        etapa = request.form.get('etapa')
        variedad = request.form.get('variedad')
        variedades = variedades_dict.get(cultivo, [])

        response = asesor.recomendar_fertilizacion(
            cultivo, suelo, clima, variedad, etapa
        )
        if 'recomendaciones' in response:
            resultado = response['recomendaciones']
            advertencias = response.get('advertencias', [])
        else:
            resultado = None
            sugerencias = response.get('sugerencias', [])

        if 'usuario_id' in session:
            guardar_consulta(session['usuario_id'], 'fertilizante', str(request.form), str(response))

    if request.method == 'GET':
        cultivo = request.args.get('cultivo', None)
        if cultivo:
            variedades = variedades_dict.get(cultivo, [])

    return render_template(
        'fertilizante.html',
        resultado=resultado,
        advertencias=advertencias,
        sugerencias=sugerencias,
        cultivos=cultivos,
        suelos=suelos,
        climas=climas,
        etapas=etapas,
        variedades=variedades
    )

@main_blueprint.route('/sintomas/<cultivo>')
def sintomas_por_cultivo(cultivo):
    sintomas = obtener_sintomas_por_cultivo(cultivo)
    return jsonify({'sintomas': sintomas})

@main_blueprint.route('/diagnostico', methods=['GET', 'POST'])
@nocache
def diagnostico():
    sugerencias = []
    quimicos = []
    cultivos = asesor.obtener_opciones('cultivos')
    sintomas_lista = asesor.obtener_opciones('sintomas')
    diagnosticos = []

    if request.method == 'POST':
        cultivo = request.form['cultivo']
        sintomas = request.form.getlist('sintomas')
        response = asesor.diagnosticar_plaga(cultivo, sintomas)
        if 'diagnosticos' in response:
            diagnosticos = response['diagnosticos']
            quimicos = response.get('quimicos_recomendados', [])
        else:
            sugerencias = response.get('sugerencias', [])

        if 'usuario_id' in session:
            guardar_consulta(session['usuario_id'], 'diagnostico', str(request.form), str(response))

    return render_template(
        'diagnostico.html',
        diagnosticos=diagnosticos,
        sugerencias=sugerencias,
        quimicos=quimicos,
        cultivos=cultivos,
        sintomas_lista=sintomas_lista
    )