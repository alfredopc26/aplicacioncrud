import pymysql
from app import app
from con import mysql
from flask import jsonify, request, flash, render_template


#GET ALL
@app.route('/')
@app.route('/select', methods=['GET'])
def lista():
    if request.method == 'GET':
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM familia")
        rows = cur.fetchall()
    return render_template("lista.html", filas=rows)

@app.route('/agregar_view', methods=['GET'])
def agregar_view():
    if request.method == 'GET':
        return render_template("agregar.html")

@app.route('/editar_view', methods=['GET'])
def editar_view():
    identificacion = str(request.args.get('id'))
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from recursos.familia where identificacion='" + identificacion + "'")
    rows = cur.fetchall()
    return render_template("modificar.html", fila=rows)


#INSERT
@app.route("/insertar", methods=["GET", "POST"])
def insertar_familia():

    if request.method == 'POST':
        identificacion = request.form['identificacion']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        celular = request.form['celular']
        estado = request.form['estado']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = "insert into familia (identificacion, nombre, apellido, edad, celular, Estado) values ('" + identificacion + "', '" + nombre + "', '" + apellido + "', '" + edad + "', '" + celular + "', '" + estado + "')"
        cur.execute(query)
        conn.commit()
        cur.close()
        output = {'identificacion' : request.form['identificacion'], 'nombre' : request.form['nombre'], 'Message': 'Success'}
    else:
        output = {'identificacion' : '', 'nombre' : '', 'Message': 'Error no type Post'}
    return jsonify({'result' : output})

#Update
@app.route('/actualizar', methods=['POST'])
def editar_familia():
    if request.method == 'POST':
        identificacion = request.form['identificacion']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        celular = request.form['celular']
        estado = request.form['estado']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = "update familia set nombre = '"+ nombre +"', apellido = '"+ apellido +"', edad = '"+ edad +"', celular = '"+ celular +"', estado = '"+ estado +"' where identificacion = '"+ identificacion +"'"
        cur.execute(query)
        conn.commit()
        cur.close()
        output = {'identificacion' : request.form['identificacion'], 'nombre' : request.form['nombre'], 'Message': 'Success'}
    else:
        output = {'identificacion' : '', 'nombre' : '', 'Message': 'Error no type Post'}
    return jsonify({'result' : output})


#DELETE
@app.route('/borrar', methods=['POST'])
def borrar_familia():
    if request.method == 'POST':
        identificacion = request.form['id']
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        query = "DELETE FROM familia where identificacion = '"+ identificacion +"'"
        cur.execute(query)
        conn.commit()
        cur.close()
        output = {'eliminado' : identificacion, 'Message': 'Success'}
    else:
        output = {'identificacion' : '', 'Message': 'Error no type Post'}
    return jsonify({'result' : output})
    
if __name__ == "__main__":
    app.debug = True
    app.run()