from flask import *
from dotenv import load_dotenv
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return ;
