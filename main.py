from flask import Flask, request, render_template,jsonify,redirect
import sqlite3

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM table_name')
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.form
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO table_name (column1, column2) VALUES (?, ?)', (data['column1'], data['column2']))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete_data/<int:id>', methods=['DELETE'])
def delete_data(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM table_name WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Row deleted successfully'})








if __name__ == '__main__':
    app.run(debug=True)
