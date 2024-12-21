# Medical-Data-Viewer
A web application built with Django and MySQL to display and analyze medical data from the FDA Adverse Event Reporting System (FAERS). Provides advanced search, data visualization, and reporting tools for better insights into adverse drug events and patient safety trends.
Prerequisites: Ensure the following are installed on your system (Note: Guide is for Windows)
1. python 3.x (Make sure it is added to system PATH)
2. MySQL Server
3. MySQL Workbench

Step 1: Import the MySQL Schema
1. Extract the project .rar file
2. Locate the G6_DB.sql file in the G6_DB_Project folder, next to the medicaldataviewer folder.
3. Open MySQL Workbench
4. Go to Server > Data Import
5. Select the G6_DB.sql file as the import source
6. Import the schema and data by following the prompts
7. Ensure that django can connect with your database
Option 1 (Preferred): Edit the MYSQL database connection settings to match the following:
Name: medicaldatav4
User: root
Password: 123
Port: 3306
Option 2: Modify the DATABASES section in the settings.py file to match your MySQL connection settings. The file can be found at:
C:\Users\yourusername\Downloads\G6_DB_Project\medicaldataviewer\myproject\settings.py
Then you can rewrite the appropriate fields with your specific MySQL connection.

Step 2: Set Up The Virtual Environment
1. Open the command terminal as an administrator
If the extracted folder is in your Downloads directory, run the following command (replace yourusername with your actual username):
2. Navigate to the extracted folder in the terminal
Assuming the extracted folder is in your downloads folder, you can run the command below, ensure you replace ‘yourusername’ with your username:
cd C:\Users\yourusername\Downloads\G6_DB_Project\medicaldataviewer
3. Run the following commands one by one:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
The terminal will show a message indicating the project is running at http://127.0.0.1:8000.
Open a browser and navigate to this URL to interact with the project.

Have fun / George Vashakidze
