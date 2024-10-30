#!/bin/bash

# Set database name and MySQL user
DB_NAME="hbtn_0d_tvshows"
MYSQL_USER="root"

# Prompt for MySQL password
read -sp "Enter MySQL password for user $MYSQL_USER: " MYSQL_PASSWORD
echo

# Create the database
echo "Creating database $DB_NAME..."
echo "CREATE DATABASE $DB_NAME;" | mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD"

# Download the SQL dump and import it
echo "Importing SQL dump..."
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$DB_NAME"

# Execute a query to select data from tv_genres
echo "Selecting data from tv_genres..."
echo "SELECT * FROM tv_genres;" | mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$DB_NAME"

echo "Done."