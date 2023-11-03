#Portafolio que sirve para mostrar los proyecto realizados por un desarrollador software

from flask import Flask, render_template, request

app = Flask(__name__)   


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')



if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)