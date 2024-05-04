from flask import Flask, request,redirect, flash , render_template
import datetime
import decimal
import config
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
app.secret_key = '12345'


"""
CORS function is to avoid No 'Access-Control-Allow-Origin' error
"""
CORS(app)

app = Flask(__name__)
app.secret_key = '12345'

# create mysql connection
db = mysql.connector.connect(host=config._DB_CONF['host'], 
                           port=config._DB_CONF['port'], 
                           user=config._DB_CONF['user'], 
                           passwd=config._DB_CONF['passwd'], 
                           db=config._DB_CONF['db'])


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

    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM persons")
        persons = cursor.fetchall()

    return render_template('index.html',persons=persons)

@app.route('/form')
def form():
    return render_template('form.html')

# Define the route for handling the form submission
@app.route('/add', methods=['POST'])
def insert():
    # Get the form data
    PersonID = int(request.form['PersonID'])
    LastName = request.form['LastName']
    FirstName = request.form['FirstName']
    Address = request.form['Address']
    City = request.form['City']

     
    with db.cursor() as cursor:
    
       query = "INSERT INTO persons (personid, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)"
    
       values = (PersonID, LastName, FirstName, Address, City)

       cursor.execute(query,values)
       db.commit()


    # Set a flash message to notify the user that the rows have been deleted
    flash(f"Data added successfully.", "success")

    # Redirect the user back to the student data page
    return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    # Get the form data
    person_id = request.form['person-id']
    last_name = request.form['last-name']
    first_name = request.form['first-name']
    address = request.form['address']
    city = request.form['city']
    
    with db.cursor() as cursor:
       cursor.execute('UPDATE persons SET lastname=%s, firstname=%s, address=%s, city=%s WHERE personid=%s', 
              (last_name, first_name, address, city, person_id))
       db.commit()

    # Redirect the user back to the student data page
    return redirect('/')

# Define the route to handle the deletion of a person
@app.route('/delete/<int:person_id>')
def delete_person(person_id):

    with db.cursor() as cursor:
       # Execute the DELETE query to remove the person from the database
       cursor.execute('DELETE FROM persons WHERE personid=%s', (person_id,))
       
       # Commit the changes to the database
       db.commit()

    # Redirect the user back to the student data page
    return redirect('/')


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='0.0.0.0', port=8080, debug=True, processes=4, threaded=True)
    app.run(host='0.0.0.0',port=8099,debug=False)
    #app.run(host='127.0.0.1', port=8080, debug=True)
## [END app]

