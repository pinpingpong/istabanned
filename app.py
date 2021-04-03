from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return "<h1 style='color: red;'>Yes</h1> <div>Last account was: oysterher</div>"

@app.route('/some_html')
def tmp():
    past_accounts = ['alt1', 'alt2']
    is_banned = "YES"
    return render_template('index.html', is_banned=is_banned, past_accounts=past_accounts)