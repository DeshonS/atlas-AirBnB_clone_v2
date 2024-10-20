-- Creates the SQL database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates user hbnbdev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- set all priviledges on database for user
GRANT ALL PRIVILEDGES ON hbnb_dev_db to 'hbnb_dev'@'localhost';

-- set select priviledges on a set database for user
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';