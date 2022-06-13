CREATE SCHEMA IF NOT EXISTS `hospital_system_final` 

CREATE TABLE IF NOT EXISTS `hospital_system_final`.`appointment` (
  `patientID` VARCHAR(50) NOT NULL,
  `apptID` INT NOT NULL UNIQUE,
  `doctorID` VARCHAR(50) NOT NULL,
  `date` VARCHAR(50) CHARACTER SET 'DEFAULT' NOT NULL,
  FOREIGN KEY ('patientID') REFERENCES PATIENT ('patientID') ON DELETE CASCADE,
  FOREIGN KEY ('doctorID') REFERENCES DOCTOR ('doctorID') ON DELETE CASCADE,
  PRIMARY KEY (`apptID`)
  );

CREATE TABLE IF NOT EXISTS `hospital_system_final`.`patient` (
  `PatientID` VARCHAR(50) NOT NULL,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NULL,
  `Age` INT NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `BloodGroup` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NULL,
  `Mobile` INT NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `RoomNumber` INT NULL,
  PRIMARY KEY (`PatientID`)
  );


CREATE TABLE IF NOT EXISTS `hospital_system_final`.`doctor` (
  `DoctorID` VARCHAR(50) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Age` VARCHAR(45) NULL,
  PRIMARY KEY (`DoctorID`)
  );


CREATE TABLE IF NOT EXISTS `hospital_system_final`.`medicalhistory` (
  `apptID` INT NOT NULL,
  `diagnosis` VARCHAR(45) NOT NULL,
  `date` VARCHAR(50) NULL,
  FOREIGN KEY ('apptID') REFERENCES APPOINTMENT ('apptID') ON DELETE CASCADE,
  PRIMARY KEY (`apptID`)
  );

INSERT INTO `hospital_system_final`.`patient`
VALUES('abc', 'aaa', 'zzz', 25, 'male', 'A+', 'Model Town, Delhi', 8918918123, asbs@xyz.com,);

INSERT INTO `hospital_system_final`.`patient`
VALUES('def', 'bbb', 'yyy', 53, 'female', 'B-', 'Vasnt Kunj', 1856382902, nwknxwn@xyz.com,);

INSERT INTO `hospital_system_final`.`patient`
VALUES('ghi', 'ccc', 'xxx', 89, 'others', 'O-', 'Greater Kailash', 3172397223327, buqbub@dtf.com);

INSERT INTO `hospital_system_final`.`patient`
VALUES('jkl', 'ddd', 'www', 12, 'male', 'B+', 'Gurgaon', 37939873988797, bjsbajs@xyz.com);

INSERT INTO `hospital_system_final`.`doctor`
VALUES('uvw', 'Sushant', '56');

INSERT INTO `hospital_system_final`.`doctor`
VALUES('xyz', 'Rakesh', '34');

INSERT INTO `hospital_system_final`.`doctor`
VALUES('rst', 'Shashank', '75');

INSERT INTO `hospital_system_final`.`medicalhistory`
VALUES('1.1', 'chest pain', '3rd April, 2021');

INSERT INTO `hospital_system_final`.`medicalhistory`
VALUES('1.2', 'cardiac arrest', '15th September, 2021');

INSERT INTO `hospital_system_final`.`medicalhistory`
VALUES('2.1', 'multiple organ failure', '20th January, 2022');

INSERT INTO `hospital_system_final`.`medicalhistory`
VALUES('3.1', 'stroken', '5th July, 2021');

INSERT INTO `hospital_system_final`.`appointment` 
VALUES ('abc', '1.3', 'uvw', '5th August 2022');

INSERT INTO `hospital_system_final`.`appointment` 
VALUES ('def', '4.1', 'uvw', '3rd May 2022');

INSERT INTO `hospital_system_final`.`appointment` 
VALUES ('ghi', '2.2', 'rst', '30th April 2022');

INSERT INTO `hospital_system_final`.`appointment` 
VALUES ('jkl', '3.2', 'xyz', '15th August 2022');

SELECT * FROM `hospital_system_final`.`patient` WHERE `PatientID` = 'abc';

SELECT 'apptID' FROM `hospital_system_final`.`medicalhistory` WHERE `apptID` = '2.1';

UPDATE `hospital_system_final`.`doctor` SET 'Age' = 58 WHERE `DoctorID` = 'xyz';

DROP TABLE `hospital_system_final`.`medicalhistory`;


