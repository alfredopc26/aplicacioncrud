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




#GET ONE
@app.route('/select/<id>', methods=['GET'])
def userone(id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM FlaskMysql WHERE NAMEID ="+id)
        rows = cur.fetchall()
        resp=jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


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
@app.route('/update/<id>', methods=['PUT'])
def updates(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    query = "update FlaskMysql set firstname = '"+ firstname +"', lastname = '"+ lastname +"' Where NameId = '"+ id +"'"
    cur.execute(query)
    conn.commit()
    cur.close()
    output = {'firstname' : request.json['firstname'], 'lastname' : request.json['lastname'], 'Message': 'Success'}


    return jsonify({'result' : output})


#DELETE
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    query = "DELETE FROM FLASKMYSQL Where NameId = '"+ id +"'"
    cur.execute(query)
    conn.commit()
    cur.close()
    output = {'firstname' : request.json['firstname'], 'lastname' : request.json['lastname'], 'Message': 'DELETED'}
    return jsonify({'result' : output})
    
if __name__ == "__main__":
    app.debug = True
    app.run()