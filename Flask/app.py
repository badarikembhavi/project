from flask import Flask, render_template, request, redirect, jsonify
import pymysql

app = Flask(__name__)

# MySQL Connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='badari',
                             database='students',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO students (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
            connection.commit()
        return jsonify({'message': 'Student registered successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
