from flask import Flask, request, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
import MySQLdb.cursors
import re  


app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@#Linkedin",
    database="user_profile_db"
)

# Define route to handle sign up form submission
@app.route('/signup', methods=['POST'])
def signup():
    # Get email and password from request body
    email = request.json['email']
    password = request.json['password']

    # Insert new user into users table
    cursor = db.cursor()
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    values = (email, password)
    cursor.execute(query, values)
    db.commit()

    # Return success response
    response = {"message": "User signed up successfully"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
