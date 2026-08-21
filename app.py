import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql', 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    active_goals = conn.execute("SELECT * FROM goals WHERE status = 'active'").fetchall()
    backlog_goals = conn.execute("SELECT * FROM goals WHERE status = 'backlog'").fetchall()
    conn.close()
    return render_template('index.html', active_goals=active_goals, backlog_goals=backlog_goals)

@app.route('/create', methods=['GET', 'POST'])
def create_goal():
    if request.method == 'POST':
        title = request.form['title']
        target_days = request.form['target_days']
        checkpoint_total = request.form['checkpoint_total']
        
        conn = get_db_connection()
        active_count = conn.execute("SELECT COUNT(*) FROM goals WHERE status = 'active'").fetchone()[0]
        
        status = 'active' if active_count < 3 else 'backlog'
        
        conn.execute(
            'INSERT INTO goals (title, target_days, checkpoint_total, status) VALUES (?, ?, ?, ?)',
            (title, target_days, checkpoint_total, status)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
        
    return render_template('new_goal.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)