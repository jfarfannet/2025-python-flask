from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/clientes')
def clientes():
    return '<h2>Lista de clientes</h2>'

@app.route('/productos')
def productos():
    return '<h2>Lista de productos</h2>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
