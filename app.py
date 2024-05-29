from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/game')
def game():
    return render_template("game.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root',
                           password='', db='proCrud')
    cursor = conn.cursor()
    cursor.execute('select * from registros order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", datos=datos)


@app.route('/agregar', methods=['GET', 'POST'])
def agrega():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        correo = request.form['correo']
        edad = request.form['edad']
        comentarios = request.form['comentarios']
        conn = pymysql.connect(
            host='localhost', user='root', password='', db='proCrud')
        cursor = conn.cursor()
        cursor.execute('insert into registros (nombre, telefono, correo, edad, comentarios) values(%s, %s, %s, %s, %s)',
                       (nombre, telefono, correo, edad, comentarios))
        conn.commit()
    return redirect(url_for('crud'))


@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='', db='procrud')
    cursor = conn.cursor()
    cursor.execute(
        'select id, nombre, telefono, correo, edad, comentarios from registros where id = %s', (id))
    dato = cursor.fetchall()
    return render_template("editar.html", datos=dato[0])


@app.route('/editarDatos/<string:id>', methods=['POST'])
def editarDatos(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        correo = request.form['correo']
        edad = request.form['edad']
        comentarios = request.form['comentarios']
        conn = pymysql.connect(
            host='localhost', user='root', passwd='', db='procrud')
        cursor = conn.cursor()
        cursor.execute('update registros set nombre=%s, telefono=%s, correo=%s,edad=%s, comentarios=%s where id=%s',
                       (nombre, telefono, correo, edad, comentarios, id))
        conn.commit()
    return redirect(url_for('crud'))


@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='', db='procrud')
    cursor = conn.cursor()
    cursor.execute('delete from registros where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))


@app.route('/demo')
def demo():
    return render_template("demo.html")


@app.route('/galery')
def galery():
    return render_template("galery.html")


if __name__ == "__main__":
    app.run(debug=True)
