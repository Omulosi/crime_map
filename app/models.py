import datetime
from .db import db

class DBHelper:

    def get_all_inputs(self):
        connection = db.get_db()
        query = "SELECT description from crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
        return cursor.fetchall()

    def add_input(self, data):
        connection = db.get_db()

        query = """INSERT INTO crimes (description) VALUES
        (%s);"""
        with connection.cursor() as cursor:
            cursor.execute(query, data)
            connection.commit()

    def clear_all(self):
        connection = db.get_db()
    
        query = "DELETE FROM crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
       

    def add_crime(self, category, date, latitude, longitude, description):
        connection = db.get_db()
        try:
            query = """INSERT INTO crimes (category, date, latitude,
            longitude, description) VALUES (%s, %s, %s, %s, %s)"""
            with connection.cursor() as cursor:
                cursor.execute(query, (category, date, latitude, longitude, description))
                connection.commit()
        except Exception as e:
            print(e)
       

    def get_all_crimes(self):
        connection = db.get_db()
        query = """SELECT latitude, longitude, date, category, description
        FROM crimes;"""
        with connection.cursor() as cursor:
            cursor.execute(query)
        named_crimes = []
        for crime in cursor:
            named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    'date': datetime.datetime.strftime(crime[2],
                        '%Y-%m-%d'),
                    'category': crime[3],
                    'description': crime[4]
                    }
            named_crimes.append(named_crime)
        return named_crimes

