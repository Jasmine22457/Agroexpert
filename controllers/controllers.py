from flask import Blueprint, render_template, request, redirect, session, url_for
from models.models import crear_usuario, verificar_usuario, guardar_consulta
from motor_inferencia.motor_inferencia import AsesorAgricola

asesor = AsesorAgricola()

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('main.home'))
    return render_template('login.html')

@main_blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = verificar_usuario(username, password)
    if user:
        session['usuario_id'] = user[0]
        session['username'] = username
        return redirect(url_for('main.home'))
    return render_template('login.html', error="Usuario o clave incorrectos.")

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        crear_usuario(request.form['username'], request.form['password'])
        return redirect(url_for('main.index'))
    return render_template('register.html')

@main_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@main_blueprint.route('/home')
def home():
    if 'usuario_id' not in session:
        return redirect(url_for('main.index'))
    return render_template('home.html', username=session['username'])

@main_blueprint.route('/fertilizante', methods=['GET', 'POST'])
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
        etapa = request.form.get('etapa')  # Puede ser None
        variedad = request.form.get('variedad')  # Puede ser None
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

@main_blueprint.route('/diagnostico', methods=['GET', 'POST'])
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

