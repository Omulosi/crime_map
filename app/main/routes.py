"""
"""
import json
from flask import Flask, render_template, request, redirect, url_for, g
from app.helpers import CATEGORIES, format_date, sanitize_string
from app.main import bp
from app.models import DBHelper

DB = DBHelper()

@bp.route("/")
def home(**kwargs):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template('home.html', crimes=crimes, 
            categories=CATEGORIES, **kwargs)


@bp.route('/submitcrime', methods=('POST',))
def submitcrime():
    error = False
    errors = {}
    category = request.form.get('category')
    if category not in CATEGORIES:
        error = True
        errors['category_error'] = 'Invalid category: Please provide a valid category'
    date = format_date(request.form.get('date'))
    if not date:
        error = True
        errors['date_error'] = 'Invalid date: Please use yyyy-mm-dd format'
    try:
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
    except ValueError:
        error = True
        errors['coordinates'] = 'Click on map to populate latitude and longitude fields'
    description = request.form.get('description')
    if not description:
        error = True
        errors['description_error'] = 'Invalid description: Please provide a valid description'
    else:
        description = sanitize_string(description)

    if error:
        return home(errors=errors, description=description, date=date, user_category=category)
    DB.add_crime(category, date, latitude, longitude, description)
    return redirect(url_for('main.home'))
