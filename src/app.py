from flask import Flask, flash, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user,login_required
from config import config   

# MODELS:
from models.ModelUser import ModelUser
# ENTITIES:
from models.entities.user import User

app = Flask(__name__)

csrf=CSRFProtect()
db=MySQL(app)
login_manager_app=LoginManager(app)

#Load de Usuario que inció la sesión
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        
        print(request.form['username'])
        print(request.form['password'])
        user= User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password: #implicitamente está la comprobacion de logged_user.password=TRUE
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Usuario o contraseña incorrecta")    
                return render_template ('auth/login.html')    
        else:
            flash("Usuario o contraseña incorrecta")    
            return render_template ('auth/login.html')
    else:
        return render_template ('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect (url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1> Esta es una vista solo para usuarios autenticados </h1>"

#Vista si intenta acceder sin estar logueado
def status_401(error):
    return redirect (url_for('login'))

#Vista si intenta acceder a una ruta que no existe
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()