import mysql.connector
from mysql.connector import errorcode

# define database credentials
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'experiolearn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/experiolearn'
# connect to database
try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Invalid username or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

# define SQL query to insert data into table
add_data = ("INSERT INTO users "
            "(name, surname, mobile_number, duration_of_stay, education_level, course_studied, university_grad_year, email, interest_areas) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

# retrieve form data from POST request
if request.method == 'POST':
  name = request.form['name']
  surname = request.form['surname']
  mobile_number = request.form['mobile_number']
  duration_of_stay = request.form['duration_of_stay']
  education_level = request.form['education_level']
  course_studied = request.form['course_studied']
  university_grad_year = request.form['university_grad_year']
  email = request.form['email']
  interest_areas = request.form['interest_areas']

  # insert form data into table
  data = (name, surname, mobile_number, duration_of_stay, education_level, course_studied, university_grad_year, email, interest_areas)
  cursor.execute(add_data, data)
  cnx.commit()

  # close database connection
  cursor.close()
  cnx.close()
