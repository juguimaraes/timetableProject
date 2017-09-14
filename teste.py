import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456790'

# Criando um banco em memoria
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/timetable_db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Flask views
@app.route('/', methods=['GET'])
def index():
    return render_template('cad_user.html')


# Flask views
@app.route('/add', methods=['POST'])
def save_user():
    try:
        # Pegando dados do formulario
        username = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        nome = request.form['nome']

        user = User(username, senha, email, nome)

        # Salvando o usuario
        db.session.add(user)
        db.session.commit()

        usuarios = User.query.all()
        return render_template("usuarios.html", usuarios=usuarios)

    except SQLAlchemyError:
        return render_template('cad_user.html')


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'user'
    username = db.Column(db.String(128), nullable=False)

    # User Name


    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False,
                      unique=True)
    password = db.Column(db.String(192), nullable=False)
    name = db.Column(db.String(128), nullable=False)
	# Nome do usuario


    # New instance instantiation procedure
    def __init__(self, username, email, password, name):
        self.name=name
        self.password=password
        self.email=email
        self.username=username


    def __repr__(self):
        mensagem = self.name + '-' + self.email + '-' + self.password

        return mensagem


if __name__ == '__main__':
    # Criando o banco
    db.create_all()
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
