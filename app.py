from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "admin123"  # Ensure the secret key is set

@app.route('/')
@app.route('/index')
def index():
    con = sql.connect("from_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/add_jogos', methods=['POST', 'GET'])
def add_jogos():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        plataforma = request.form['plataforma']
        con = sql.connect("from_db.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (nome, genero, ano, plataforma) VALUES (?, ?, ?, ?)", (nome, genero, ano, plataforma))
        con.commit()
        flash("Jogo adicionado com sucesso", "success")
        return redirect(url_for("index"))
    return render_template("add_jogos.html")

@app.route('/editar_jogos/<string:id>', methods=['POST', 'GET'])
def editar_jogos(id):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        plataforma = request.form['plataforma']
        con = sql.connect("from_db.db")
        cur = con.cursor()
        cur.execute("UPDATE users SET nome=?, genero=?, ano=?, plataforma=? WHERE id=?", (nome, genero, ano, plataforma, id))
        con.commit()
        flash("Jogo editado com sucesso", "success")
        return redirect(url_for("index"))
    con = sql.connect("from_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users WHERE id=?", (id,))
    data = cur.fetchone()
    return render_template("editar_jogos.html", datas=data)

@app.route('/deletar_jogos/<string:id>', methods=['GET'])
def deletar_jogos(id):
    con = sql.connect("from_db.db")
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (id,))
    con.commit()
    flash("Jogo deletado", "warning")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)