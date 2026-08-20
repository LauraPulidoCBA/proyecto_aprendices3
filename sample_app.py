from flask import Flask, render_template, request, redirect
import pymysql
import os

sample = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@sample.route("/", methods=["GET"])
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM aprendices")
        aprendices = cursor.fetchall()
        conn.close()
        db_status = "Conexión exitosa a la BD!"
    except Exception as e:
        aprendices = []
        db_status = f"Error en la conexión: {e}"

    return render_template("index.html", aprendices=aprendices, db_status=db_status, ci_cd_text="Prueba para CI/CD")

@sample.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre_completo"]
    documento = request.form["numero_documento"]
    ficha = request.form["ficha"]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO aprendices (nombre_completo, numero_documento, ficha) VALUES (%s, %s, %s)",
        (nombre, documento, ficha)
    )
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == '__main__':
    sample.run(host="0.0.0.0", port=5050, debug=True)