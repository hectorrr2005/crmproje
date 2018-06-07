from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemySessionUserDatastore, login_required, utils
from database import db_session, init_db
from models import User, Role


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'test'


# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

@app.route('/')
@login_required
def default():
    return render_template('index.html')

@app.route('/widgets')
@login_required
def widgets():
    return render_template('widgets.html')



app.run(debug=True)