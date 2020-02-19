from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route('/home')
def home():
    e = ['SIMPRAD', 'Semana Ads', 'Semana da Ciência do x-bacon']
    return render_template('index.html', eventos=e)
