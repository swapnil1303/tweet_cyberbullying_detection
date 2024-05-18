from flask import *
from random import randint
import sqlite3 as sql
from functions import *
from datetime import datetime
import pickle
app = Flask(__name__)
app2=Flask(__name__)
app.secret_key="swapnil"
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']

        # Debugging prints
        print(f"Received data - Email: {email}, Username: {username}, Password: {password}, Phone: {phone}, Address: {address}")

        # Connect to the database
        con = sql.connect('child_proj.db')
        cur = con.cursor()

        # Insert data into the register table
        cur.execute('INSERT INTO register (email, username, password, phone, address) VALUES (?, ?, ?, ?, ?)',
                    (email, username, password, phone, address))
        
        con.commit()
        con.close()

        return redirect(url_for('login'))

        

    return render_template('register.html')


# code by swap2

@app.route('/login',methods=['POST','GET'])
def login():
    
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        
        con  = sql.connect('child_proj.db')
        cur = con.cursor()
        
        cur.execute('select username,password from register where username=? and password=?',(username,password))
        data = cur.fetchone()
        print(data)
        # if data is None:
        #     return render_template('login.html', error='Invalid username or password', invalid='your are invalid user')
        if data is None:
            return render_template('login.html', error='Invalid username or password', invalid='your are invalid user')

        # Check if the email matches but the password does not
        if data[1] != password:
            return render_template('login.html', error='Unauthorized access', invalid='')

        # Check if the email does not match
        if data[0] != username:
            return render_template('login.html', error='Invalid user', invalid='')
        return render_template('home.html',name=username)
    
    return render_template('login.html')


@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        message=request.form['tweet']
        print(message)
        return render_template("home.html",name=message)
    return render_template("home.html")
    
@app.route('/prediction',methods=['POST','GET'])
def prediction():
    if request.method == 'POST':
        message=request.form['tweet']
        if(message==""):
            return render_template("home.html",error="Please enter a message to continue..")
        prediction = custom_input_prediction(message)
        print(prediction)
       
        return render_template("prediction.html",prediction=prediction,message=message)


if __name__ == '__main__':
    app.run(debug=True)