CREATE DATABASE demodb;
USE demodb;
CREATE TABLE `demodb`.`employee` (  `emp_id` INT NOT NULL,  `name` VARCHAR(45),  `salary` INT,  PRIMARY KEY (`emp_id`));
CREATE USER 'demouser'@'%' IDENTIFIED BY 'eafit';
GRANT ALL PRIVILEGES ON demodb.* TO 'demouser'@'%';
