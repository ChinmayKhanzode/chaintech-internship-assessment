from flask import Flask, render_template, request, redirect, url_for
import sqlite3
    
app = Flask(__name__)

conn = sqlite3.connect('employees.db',check_same_thread=False)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        empid TEXT NOT NULL,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        department TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')
conn.commit()


@app.route('/', methods=['GET', 'POST'])
def register_employee():
    
    return render_template('index.html',)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        
        empid = request.form.get('empid')
        name = request.form.get('name')
        date = request.form.get('date')
        department = request.form.get('department')
        description = request.form.get('description')

        cursor.execute(f'INSERT INTO employees (empid,name,date,department,description) VALUES (?,?,?,?,?)', (empid,name,date,department,description))
        conn.commit()
        print("Inserted")
    return render_template('form.html')


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    cursor.execute('SELECT * FROM employees')
    data = cursor.fetchall()
    return render_template('employeeslist.html',all = data)



if __name__ == '__main__':
    app.run(debug=True)
