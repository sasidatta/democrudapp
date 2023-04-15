import logging

from flask import Flask, request,redirect, flash , render_template
import datetime
import decimal
import pymysql
import json
import config
from flask_cors import CORS
import MySQLdb

app = Flask(__name__)
app.secret_key = 'i23jeij23eijii32ui23uiui23ui32u32i'

"""
CORS function is to avoid No 'Access-Control-Allow-Origin' error
"""
CORS(app)

def type_handler(x):
    """type Serialization function.

    Args:
        x:

    Returns:
        Serialization format of data, add more isinstance(x,type) if needed
    """
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    if isinstance(x, decimal.Decimal):
        return '$%.2f'%(x)
    raise TypeError("Unknown type")

@app.route('/')
def index():
    """webserice test method
    """

    # create mysql connection
    conn = MySQLdb.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])

    cur = conn.cursor (MySQLdb.cursors.DictCursor)
    sql="select * from persons;"
    cur.execute(sql)
    
    # get all column names
    columns = [desc[0] for desc in cur.description]
    # get all data
    rows=cur.fetchall()
    
    cur.close()
    conn.close()

    return render_template('index.html',headers=columns,rows=rows)

@app.route('/form')
def form():
    return render_template('form.html')

# Define the route for handling the form submission
@app.route('/insert', methods=['POST'])
def insert():
    # Get the form data
    PersonID = request.form['PersonID']
    LastName = request.form['LastName']
    FirstName = request.form['FirstName']
    Address = request.form['Address']
    City = request.form['City']

     
    # create mysql connection
    conn = MySQLdb.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])

    # Insert the data into the MySQL table
    
    cursor = conn.cursor()

    query = "INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)"
    
    values = (PersonID, LastName, FirstName, Address, City)

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()

    # Set a flash message to notify the user that the rows have been deleted
    flash(f"Data added successfully.", "success")

    # Redirect the user back to the student data page
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    # Get the list of row IDs to delete
    rows_to_delete = request.form.getlist('delete[]')
 
    if len(rows_to_delete) > 0:
        try:
            # Delete the selected rows from the database
                # create mysql connection
            conn = MySQLdb.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])

            cursor = conn.cursor()
            query = "DELETE FROM Persons WHERE PersonID IN (%s)"
            placeholders = ', '.join(['%s'] * len(rows_to_delete))
            query = query % placeholders
            cursor.execute(query, tuple(rows_to_delete))
            conn.commit()

            # Set a flash message to notify the user that the rows have been deleted
            flash(" row(s) deleted successfully.", "success")

        except Exception as e:
                print(e)
                flash("An error occurred while deleting the data")
        
        finally:
                cursor.close()
                conn.close()

    # Redirect the user back to the student data page
    return redirect('/')



@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='0.0.0.0', port=8080, debug=True, processes=4, threaded=True)
    app.run(port=8099,debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
## [END app]

