-- Script to create the database hbtn_0d_2 and the MySQL user user_0d_2 with SELECT privilege.
-- If the database hbtn_0d_2 already exists, the script will not fail.
-- If the user user_0d_2 already exists, the script will not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
