from flask import Flask, request, render_template, url_for, redirect,session
from logic.model import db, Appointment
from datetime import datetime  
import os
import json

def create_app():
    
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET KEY'] = 'password'

 
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

def cargar_datos():
    users_file_path = os.path.join("data", "users.json")
    admin_file_path = os.path.join("data", "admin.json")

    with open(users_file_path, 'r') as users_file:
        users = json.load(users_file)
    with open(admin_file_path, 'r') as admin_file:
        admin = json.load(admin_file)
    return users, admin

@app.route('/schedule', methods=['POST']) 
def schedule_appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    date_str = request.form.get('date')
    time_str = request.form.get('time')
    
    date1 = datetime.strptime(date_str, '%Y-%m-%d').date()
    time1 = datetime.strptime(time_str, '%H:%M').time()
    
    appointment = Appointment(name=name,email=email, date=date1, time=time1)
    db.session.add(appointment) # agregar 
    db.session.commit()
    
    return redirect(url_for("agenda"))


@app.route('/delete/<int:id>', methods=['GET','POST']) 
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    
    if appointment:
        db.session.delete(appointment) # eliminar
        db.session.commit()
    return redirect(url_for("view_appointments"))

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/usuario')
def usuario():
    if 'username' in session:
        username = session['username']  # Obtén el nombre de usuario de la sesión
        return render_template('usuario.html', user_name=username)
    else:
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        code = request.form.get('code')

        users, admin = cargar_datos()

        if username in users and password == users[username]:
            session['username'] = username
            return redirect(url_for('usuario'))
        elif username in admin and password == admin[username]["password"]:
            if 'code' in admin[username] and code == admin[username]['code']:
                session['username'] = username
                return redirect(url_for('admin'))
            else:
                error_message = "Código de administrador incorrecto"
                return render_template('login.html', error=error_message)
        else:
            error_message = "Credenciales incorrectas"
            return render_template('login.html', error=error_message)

    return render_template('login.html')
    
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        code = request.form.get('code')

        users, admin = cargar_datos()

        if username in users or username in admin:
            error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            return render_template('registro.html', error=error_message)

        if password == confirm_password:
            if code:
                # Registro como administrador
                admin[username] = {
                    "password": password,
                    "code": code
                }
                with open(os.path.join("data", "admin.json"), 'w') as admin_file:
                    json.dump(admin, admin_file)
            else:
                # Registro como usuario
                users[username] = password
                with open(os.path.join("data", "users.json"), 'w') as users_file:
                    json.dump(users, users_file)

            success_message = "Registro exitoso. Ahora puedes iniciar sesión."
            return render_template('registro.html', success=success_message)
        else:
            error_message = "Las contraseñas no coinciden."
            return render_template('registro.html', error=error_message)

    return render_template('registro.html')

@app.route('/agendamiento')
def agenda():
    return render_template ('agendamiento.html')

@app.route('/lista_citas')
def view_appointments():
    appointments = Appointment.query.all()
    return render_template('lista_citas.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)