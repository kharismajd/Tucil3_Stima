from flask import Flask,request,render_template
from graph import *

app = Flask(__name__)

@app.route('/')
def home():
    print("Masukkan nama file:")
    file_name = input()
    graph = Graph("../test/" + file_name)
    return render_template('main.html', graph = graph)

if __name__ == '__main__':
    app.run()