from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Statusu 'active' olanları götür
    active_goals = conn.execute("SELECT * FROM goals WHERE status = 'active'").fetchall()
    # Statusu 'backlog' olanları götür
    backlog_goals = conn.execute("SELECT * FROM goals WHERE status = 'backlog'").fetchall()
    conn.close()
    return render_template('index.html', active_goals=active_goals, backlog_goals=backlog_goals)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        target_days = request.form['target_days']
        checkpoint_total = request.form['checkpoint_total']
        
        conn = get_db_connection()
        # Hal-hazırda neçə aktiv goal olduğunu sayırıq
        active_count = conn.execute("SELECT COUNT(*) FROM goals WHERE status = 'active'").fetchone()[0]
        
        # Əgər 3-dən azdırsa 'active', yoxsa 'backlog' elə
        status = 'active' if active_count < 3 else 'backlog'
        
        conn.execute(
            "INSERT INTO goals (title, target_days, checkpoint_total, checkpoint_done, status) VALUES (?, ?, ?, ?, ?)",
            (title, target_days, checkpoint_total, 0, status)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
        
    return render_template('new_goal.html')

if __name__ == '__main__':
    app.run(debug=True)