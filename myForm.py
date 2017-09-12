from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD1_REGEX = re.compile(r'[A-Z0-9]')
# PASSWORD_REGEX = re.compile(r'[0-9]')
app = Flask(__name__)
app.secret_key = 'thisIsASecretKeepItThatWay'

@app.route('/')

def registForm():

    return render_template('form.html')

@app.route('/result', methods=['POST'])

def displayResult():

    if len(request.form['name']) < 1:
        flash('Must fill out all text areas!', 'error')
        return render_template('error.html')
    elif len(request.form['email']) < 1:
        flash('Must fill out all text areas!', 'error')
        return render_template('error.html')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address!', 'error')
        return render_template('error.html')
    elif len(request.form['password']) < 1:
        flash('Must fill out all text areas!', 'error')
        return render_template('error.html')
    elif len(request.form['password1']) < 1:
        flash('Must fill out all text areas!', 'error')
        return render_template('error.html')
    elif str(request.form['password']) != str(request.form['password1']):
        flash('Passwords must match!')
        return render_template('error.html')
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'error')
        return render_template('error.html')
    elif not PASSWORD1_REGEX.match(request.form['password']):
        flash('Password must contain [a-zA-Z0-9]')
        return render_template('error.html')
    # elif not PASSWORD_REGEX.match(request.form['password']):
    #     flash('Password must contain [a-zA-Z0-9]')
    #     return render_template('error.html')
    else:
        return render_template('result.html')

    return render_template('result.html')

app.run(debug=True)