from dbhelper import DBHelper
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return render_template('home.html', data=data)

@app.route('/add', methods=('GET', 'POST'))
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as e:
        print(e)
    return redirect(url_for('home'))

@app.route('/clear', methods=('GET', 'POST'))
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return redirect(url_for('home'))

@app.route('/submitcrime', methods=('POST',))
def submitcrime():
    category = request.form.get('category')
    date = request.form.get('date')
    latitude = float(request.form.get('latitude'))
    longitude = float(request.form.get('longitude'))
    description = request.form.get('description')
    DB.add_crime(category, date, latitude, longitude, description)
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)