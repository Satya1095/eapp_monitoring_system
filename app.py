#E-APP monitoring system- main application
#flask_libraries
from flask import Flask, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error
from flask_googlemaps import GoogleMaps
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)

#setup and configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:project1@localhost:3306/monitor'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['GOOGLEMAPS_KEY'] = "AIzaSyC_Q7ZPtlCx89fC_4vWPOoUeZEBnDcS9rA"
app.config['SECRET_KEY'] = "key"
GoogleMaps(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_fxn = LoginManager()
login_fxn.init_app(app)
login_fxn.login_view = 'login'

#loginform
class login_form(FlaskForm):
    Username = StringField('Username:', validators=[InputRequired()])
    Password = PasswordField('Password:', validators=[InputRequired()])

#database_table_entries for validation of loginform
class User(UserMixin, db.Model):
    tablename = "User"
    UserId = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(30))
    UserPassword = db.Column(db.String(30))
    def get_id(self):
        return (self.UserId)
@login_fxn.user_loader
def userid(UserId):
    return User.query.get(int(UserId))

#application routing and defnitions
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')
        
@app.route('/users')
def users():
    try:
        connection = mysql.connector.connect(host='localhost',
                                     database='monitor',
                                     user='root',
                                     password='project1')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM IncidentExchange ORDER BY Timestamp DESC LIMIT 10')
            users = cursor.fetchall()
            return render_template('users.html', users= users)
    except Error as e:
        print("Error connecting",e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()

@app.route('/user/')
@login_required
def user():
    return render_template('user.html', NAME=current_user.UserName, ID=current_user.UserId)   
#userlogin
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form()
    #login-validation
    if form.validate_on_submit():
        user = User.query.filter_by(UserName= form.Username.data).first()
        if user:
            if user.UserPassword == form.Password.data:
                login_user(user)
                return redirect(url_for('user'))
        return 'Invalid Username or Password'
    return render_template('login.html', form=form)
#userlogout        
@app.route('/user/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user/userdata')
def userdata():
    try:
        connection = mysql.connector.connect(host='localhost',
                                     database='monitor',
                                     user='root',
                                     password='project1')
        if connection.is_connected():
            cursor = connection.cursor()
            ID= current_user.UserId
            sql_query= """SELECT * FROM IncidentExchange WHERE UserId = %s"""
            cursor.execute(sql_query, (ID, ))
            userdata = cursor.fetchall()
            return render_template('userdata.html', userdata= userdata, NAME=current_user.UserName, ID=current_user.UserId)
    except Error as e:
        print("Error connecting",e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()

@app.route('/user/map')
def map():
    return render_template('map.html', ID=current_user.UserId, NAME=current_user.UserName)
@app.route('/user/graph', methods=['GET', 'POST'])
def graph():
    return render_template('graph.html', ID=current_user.UserId, NAME=current_user.UserName )


if __name__ == '__main__':
    app.run(debug='True')   
