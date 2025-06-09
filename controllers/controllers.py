from flask import Blueprint, render_template, request, redirect, session, url_for
from models.models import crear_usuario, verificar_usuario, guardar_consulta
from motor_inferencia.motor_inferencia import recomendar_fertilizante, diagnosticar_plaga, recomendar_acuaponia
from base_conocimiento.base_conocimiento import CULTIVOS, SUELOS, CLIMAS, PECES, CULTIVOS_ACUA, SINTOMAS

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
    if request.method == 'POST':
        cultivo = request.form['cultivo']
        suelo = request.form['suelo']
        clima = request.form['clima']
        resultado = recomendar_fertilizante(cultivo, suelo, clima)
        if 'usuario_id' in session:
            guardar_consulta(session['usuario_id'], 'fertilizante', str(request.form), resultado)
    return render_template('fertilizante.html', resultado=resultado, cultivos=CULTIVOS, suelos=SUELOS, climas=CLIMAS)

@main_blueprint.route('/diagnostico', methods=['GET', 'POST'])
def diagnostico():
    resultado = None
    sintomas = []
    if request.method == 'POST':
        cultivo = request.form['cultivo']
        sintomas = request.form.getlist('sintomas')
        resultado = diagnosticar_plaga(cultivo, sintomas)
        if 'usuario_id' in session:
            guardar_consulta(session['usuario_id'], 'diagnostico', str(request.form), resultado)
    return render_template('diagnostico.html', resultado=resultado, cultivos=CULTIVOS, sintomas_lista=SINTOMAS, sintomas=sintomas)

@main_blueprint.route('/acuaponia', methods=['GET', 'POST'])
def acuaponia():
    resultado = None
    if request.method == 'POST':
        pez = request.form['pez']
        cultivo = request.form['cultivo']
        resultado = recomendar_acuaponia(pez, cultivo)
        if 'usuario_id' in session:
            guardar_consulta(session['usuario_id'], 'acuaponia', str(request.form), resultado)
    return render_template('acuaponia.html', resultado=resultado, peces=PECES, cultivos=CULTIVOS_ACUA)
