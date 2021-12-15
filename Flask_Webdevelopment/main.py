import datetime, socket
import logging
import time
from datetime import timedelta   # import to make session longer in the browser
from logging import ERROR
from time import strftime
import sqlite3 as sql
from _sqlite3 import Connection
from werkzeug.utils import redirect
from flask import Flask, render_template,url_for, request, flash, session
from passlib.hash import sha256_crypt
from forms import RegistrationForm, LoginForm,updatePasswordForm



logger=logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
#f = logging.Formatter=('%(asctime)s -  %(levelname)s - %(message)s')
fh = logging.FileHandler('logFile.log')
#fh.setFormatter(f)
logger.addHandler(fh)


connection = sql.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
    connection.cursor()
connection.commit()
connection.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# logging.basicConfig(filename='demo.log', level=logging.ERROR,
#                     format='%(asctime)s -  %(levelname)s - %(message)s')
# logging.basicConfig(filename='record.log', level=logging.warning("Warning message"),
#                      format=f'%(asctime)s  : %(message)s')


# file_handler = FileHandler('errorlog.txt')
# file_handler.setLevel(WARNING)    
#main.py.logging.addHandler(file_handler)


@app.route('/')
@app.route('/index.html')
def index():
    """display index page."""   
    return render_template('index.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))

@app.route("/register.html", methods=['POST', 'GET'])
def register():
    """Deplay registration function"""
    form=RegistrationForm()
    error = None
    if request.method=='POST':        
        username = request.form['username']
        password = request.form['password']
        
        error = None
        if not complex(password):
            error='Need complex password'
            flash(error)
            return render_template('register.html',form = form, error=error)
        else:
            con=sql.connect('database.db')
            c=con.cursor()     
            hash_pass = sha256_crypt.hash(password)
            statement = f"SELECT username from users WHERE username='{username}';"    
            c.execute(statement)
            data=c.fetchone()
            print(data)
            if not data:
                c.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,hash_pass))
                con.commit()
                con.close()
                error ='User is registered successfully.'
                flash(error)
                return redirect('login.html')                
            elif data:                
                for i in data:                    
                    if(username != i):                                        
                        c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username,hash_pass))
                        con.commit()
                        con.close()
                        flash('User is registered successfully.')
                        return redirect(url_for('login'))
                    else:                        
                        flash('User is already registered')
                        return render_template('register.html',form = form, error=error)
    if request.method=='GET':
        return render_template('register.html', form = form)
 

@app.route('/login.html', methods=['POST', 'GET'])
def login():
    """Deplay login function"""    
    form=LoginForm()    
    if request.method=='POST': 
        app.permanent_session_lifetime = timedelta(minutes=5)   
        #session.permanent = True       
        username = request.form['username']
        password = request.form['password']
        session["user"] = username
        con=sql.connect('database.db')
        c=con.cursor()
        hash_pass = sha256_crypt.hash(password)
        statement=f"SELECT username, password from users WHERE username='{username}';"
        c.execute(statement)
        data=c.fetchone()
        h_name = socket.gethostname()
        ip_address = socket.gethostbyname(h_name)
        date = time.strftime("%m/%d/%Y %H:%M:%S")     
        if not data:
            flash("Not a register user.")
            return render_template('login.html', form=form)
        elif data:                             
            for i in data:                
                if((username == data[0])and (sha256_crypt.verify(password, data[1]))):
                    session["loggedin"] =True
                    session["user"] = username
                    return redirect(url_for('home'))             
                    
                else:                
                    flash("Invalid password")
                    error="Invalid password"
                    logger.error(f'{date:<12}--{ip_address:<12}--{error}')
                    return render_template('login.html', form=form)    
    elif request.method=='GET':
        return render_template('login.html', form=form)


def textfile_to_list():
    """store common password in a list"""
    file = open('CommonPassword.txt', 'r')
    f = file.readlines()
    newList = []
    for line in f:
        if line[-1] == '\n':
            newList.append(line[:-1])

        else:
            newList.append(line)
    return newList


def compare_secrets(password):
    """compare given password with common password list"""
    password_list = []
    password_list = textfile_to_list()
    for item in password_list:
        if item == password:
            return True
    return False

@app.route('/updatePassword.html',methods=['POST', 'GET'])
def updatePassword():
    form=updatePasswordForm()
    if request.method=='POST':
        newpassword=request.form['newpassword']  
        username = user()    # session username function
        if not compare_secrets(newpassword):
            if complex(newpassword):
                error = None
                hash_pass=sha256_crypt.hash(newpassword)
                con=sql.connect('database.db')
                c=con.cursor()
                c.execute(f"UPDATE users set password ='{hash_pass}' WHERE username = '{username}';")
                con.commit()
                print("successful")
                con.close()
                return redirect('login.html')
            else:
                flash("Need complex password")
                return redirect('updatePassword.html')
        else:
            flash("Chosen password is found in a common password list.\
                                    \n Please select different password.")
            return redirect('updatePassword.html')
        
    return render_template('updatePassword.html', form=form)

def checknotreg(username):
    """ check username in db"""
    con=sql.connect('database.db')
    c=con.cursor()
    statement = f"SELECT username from users WHERE username='{username}';"    
    c.execute(statement)
    data=c.fetchone()
    if data:
        return True 
    
def complex(password):
    """  return true if password as per specification"""   
    if (any(c.islower() for c in password) and any(u.isupper() for u in password)
            and any(n.isdigit() for n in password)):
        return True
    
@app.route("/user")
def user():
    if user in session:
        user=session[user]       
        return user
    else:
        return render_template("login.html")
    
@app.route('/logout')
def logout():
    session.pop("user",None)
    return render_template("index.html")
    
    

@app.route('/home.html')
def home():
    """display home page."""
    return render_template('home.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))

@app.route('/python_overview.html')
def overview():
    """display python_overview.html."""
    return render_template('python_overview.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))

@app.route('/useful_python_links.html')
def resouces():
    """display useful_python_links.html."""
    return render_template('useful_python_links.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))

@app.route('/basic_syntax.html')
def syntax():
    """display basic_syntax.html."""
    return render_template('basic_syntax.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))

@app.route('/data_structure.html')
def data():
    """display data_structure page."""
    return render_template('data_structure.html', date = time.strftime("%m/%d/%Y %H:%M:%S"))
       
@app.route('/errorLog',methods=['POST','GET'])
def errorLog(error):    
    h_name = socket.gethostname()
    ip_address = socket.gethostbyname(h_name)        # print("Host Name is:" + h_name)
    print("Computer IP Address is:" + ip_address)
    date = time.strftime("%m/%d/%Y %H:%M:%S")
        # logging.basicConfig(level=logging.ERROR,
        #             format=f'{date} {ip_address:<20} ',
        #             style='{',
        #             filename='logfile.log', 
        #             filemode='w')
    logging.basicConfig(filename='record.log', level=logging.error(error),
                      format=f'{date} {ip_address:<20}' )  
    



if __name__ == '__main__':
    app.run(debug=False)