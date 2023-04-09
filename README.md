# About the project

The presented models gives the user an overview of how database systems
are put to use in real life scenarios by taking a hospital as an example.
The model accounts for appointments between the patient and the doctor, the
patient’s past medical history and
Functional Requirement -
The model utilizes the tkinter package of Python and HTML to structure the
front end of the system.
The code for the various components of the database has been executed and run on
Microsoft Workbench

### Schema
![schema image](https://github.com/debjit15005/HMS/blob/main/assets/hospitaldbschema.png?raw=true)

### Entity Relationship Diagram
![er diagram](https://github.com/debjit15005/HMS/blob/main/assets/ER.jpeg)

### Data Normalization
Functional Dependencies -

Patient : 
{PatientID, FirstName, LastName, Mobile, Email, RoomNumber, Gender, Address, Age, BloodGroup}

Appointment :
{apptID, patientID, date, doctorID}

Medical History :
{apptID, date , diagnosis}

Doctor :
{doctorID, name, age}

On basis if the functional dependencies that exist in the table, we realize that the entire database has been normalized upto 3 NF. 

### Table Utilized
* Patient 
* Doctor 
* Appointment 
* Medical History 

Relations between the tables -
* Books between tables Patient and Appointment to signify the patient’s competency to book an appointment. The relation is a 1 : N relation. 
* Takes between tables Doctor and Appointment to signify the doctor’s vacancy to take a consultation. The relation is a 1 : 1 relation.
* Record between tables Appointment and Medical History to demonstrate the pass record of a patient 

## Snapshot of the app
![app](https://github.com/debjit15005/HMS/blob/main/assets/app_snapshot.png)
