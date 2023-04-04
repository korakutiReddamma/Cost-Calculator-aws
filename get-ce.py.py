import sqlite3
import flask


app = flask.Flask(__name__)
@app.route('/cost')
def display_data():
    conn = sqlite3.connect('database_name.db')
    cursor = conn.execute('SELECT * FROM mock_data')
    data = cursor.fetchone()
    print(data[0],data[1],data[2])
    conn.close()
    return flask.render_template("data.html",data=data)
@app.route('/costdata')
def display_data1():
    conn = sqlite3.connect('database_name.db')
    cursor = conn.execute('SELECT * FROM mock_data')
    data = cursor.fetchone()
    print(data[0],data[1],data[2])
    conn.close()
    return flask.render_template("view.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)
