from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemy

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'usbw'
app.config['MYSQL_DATABASE_DB'] = 'timetable_db'

mysql.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('cad_user.html')

@app.route('/add', methods=['POST'])
def save_user():
	usuario = request.form['usuario']
	senha = request.form['senha']
	email = request.form['email']
	nome = request.form['nome']
	cur = mysql.get_db().cursor()
	cur.execute('''INSERT INTO usuarios (Nome, Usuario, Senha, Email) VALUES (%s, %s, SHA1(%s), %s) ''', (nome, usuario, senha, email))

if __name__ == '__main__':
	app.run(debug=True)


