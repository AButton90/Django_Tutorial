# Install MySQL on pc https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Root1234!"
)

# prepare a cursor object using cursor() method
cursor = data_base.cursor()

# create database
cursor.execute("CREATE DATABASE anel_co")
