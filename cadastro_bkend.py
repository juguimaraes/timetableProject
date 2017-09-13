from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3307
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'usbw'
app.config['MYSQL_DATABASE_DB'] = 'cadastro1'

mysql.init_app(app)

@app.route('/', methods=['POST'])
def index():
	usuario = request.form['usuario']
	senha = request.form['senha']
	email = request.form['email']
	nome = request.form['nome']
	cur = mysql.get_db().cursor()
	cur.execute('''INSERT INTO cadastro1 (Nome, Usuario, Senha, Email) VALUES (%s, %s, SHA1(%s), %s) ''', (nome, usuario, senha, email))

if __name__ == '__main__':
	app.run(debug=True)


