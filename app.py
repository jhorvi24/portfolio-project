#Portafolio que sirve para mostrar los proyecto realizados por un desarrollador software

from flask import Flask, render_template, request
import socket

app = Flask(__name__)  
app._static_folder = 'static'

def get_ip():    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

@app.route('/')
def index():
    hostname, ip = get_ip()    
    return render_template('index.html', HOSTNAME=hostname, IP=ip)  
    

@app.route('/perfil')
def perfil():
    hostname, ip = get_ip()    
    return render_template('perfil.html')

@app.route('/proyectos')
def proyectos():
    hostname, ip = get_ip()    
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():        
    return render_template('contacto.html')
    



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)