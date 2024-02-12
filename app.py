from flask import Flask, render_template, request, redirect, session
from db import DataBase
import api
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
dbo = DataBase()
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_naam')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message='Registration successful, \n'
                                                     'proceed to login')
    else:
        return render_template('register.html', message='Email already exist\n')
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    response = dbo.search(email, password)
    if response:
        session['logged-in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message='Email/password incorrect\n')
@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')
@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')
@app.route('/perform_ner', methods=['post'])
def perform_ner():
    if session:
        text=request.form.get('Text-area')
        response = api.ner(text)
        return render_template('ner.html', response=response)
    else:
        return redirect('/')
@app.route('/sentimentanalysis')
def sentimentanalysis():
    if session:
        return render_template('sentimentanalysis.html')
    else:
        return redirect('/')

@app.route('/perform_sentimentanalysis', methods=['post'])
def perform_sentimentanalysis():
    if session:
        text=request.form.get('Text-area')
        response = api.senti(text)
        a = 0
        b = ''
        for i in response['sentiment']:
            if a < response['sentiment'][i]:
                a = response['sentiment'][i]
                b = i
        return render_template('sentimentanalysis.html', response=f'{b} ==>>> {a}')
    else:
        return redirect('/')
@app.route('/abusedetection')
def abusedetection():
    if session:
        return render_template('abusedetection.html')
    else:
        return redirect('/')
@app.route('/perform_abusedetection', methods=['post'])
def perform_abusedetection():
    if session:
        text=request.form.get('Text-area')
        response = api.abuse(text)
        result = {}
        for i in response:
            result[i] = str(response[i])
        return render_template('abusedetection.html', response=result)
    else:
        return redirect('/')
if __name__ == "__main__":
    app.run()
