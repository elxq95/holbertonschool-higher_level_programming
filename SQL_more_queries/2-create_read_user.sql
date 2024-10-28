-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Create the database hbtn_0d_2 if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2 with a password, only if the user doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;