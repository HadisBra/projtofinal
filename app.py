import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "admin123"  # Ensure the secret key is set


def get_db_connection():
    """Create and return a database connection."""
    conn = sql.connect("from_db.db")
    conn.row_factory = sql.Row
    return conn


@app.route('/')
@app.route('/index')
def index():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    con.close()
    return render_template('index.html', datas=data)


@app.route('/add_jogos', methods=['POST', 'GET'])
def add_jogos():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        plataforma = request.form['plataforma']
        con = get_db_connection()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO users (nome, genero, ano, plataforma) VALUES (?, ?, ?, ?)",
                        (nome, genero, ano, plataforma))
            con.commit()
            flash("Jogo adicionado com sucesso", "success")
        except sql.Error as e:
            flash(f"Erro ao adicionar jogo: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))
    return render_template("add_jogos.html")


@app.route('/editar_jogos/<int:id>', methods=['POST', 'GET'])
def editar_jogos(id):
    con = get_db_connection()
    cur = con.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = request.form['ano']
        plataforma = request.form['plataforma']
        try:
            cur.execute("UPDATE users SET nome=?, genero=?, ano=?, plataforma=? WHERE id=?",
                        (nome, genero, ano, plataforma, id))
            con.commit()
            flash("Jogo editado com sucesso", "success")
        except sql.Error as e:
            flash(f"Erro ao editar jogo: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))

    cur.execute("SELECT * FROM users WHERE id=?", (id,))
    data = cur.fetchone()
    con.close()

    if data is None:
        flash("Jogo não encontrado", "warning")
        return redirect(url_for("index"))

    return render_template("editar_jogos.html", datas=data)


@app.route('/deletar_jogos/<int:id>', methods=['GET'])
def deletar_jogos(id):
    con = get_db_connection()
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id=?", (id,))
        con.commit()
        flash("Jogo deletado", "warning")
    except sql.Error as e:
        flash(f"Erro ao deletar jogo: {e}", "danger")
    finally:
        con.close()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
