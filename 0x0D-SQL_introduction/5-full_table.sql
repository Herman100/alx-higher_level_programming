-- Script to print the full description of the table first_table
-- from the database hbtn_0c_0 in the MySQL server

-- Get the database name from the command line argument
database_name=$1

-- Connect to the database
mysql -u root -p $database_name

-- Get the create table statement for the first_table table
create_table_statement=`SHOW CREATE TABLE first_table`;

-- Print the create table statement
echo "$create_table_statement"
