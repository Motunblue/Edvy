-- Prepares MYSQL server for Edvy

-- create database
CREATE DATABASE IF NOT EXISTS Edvy_db;
CREATE USER IF NOT EXISTS 'edvy_user'@'localhost' IDENTIFIED BY 'edvy_dev_pwd';
GRANT ALL PRIVILEGES ON `Edvy_db`.* TO 'edvy_user'@'localhost';

FLUSH PRIVILEGES;
