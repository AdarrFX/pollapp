# Polling Application

## How to setup and run

### Description

This is a python-django application designed to allow users to login and vote on poll options created by an admin. This readme details how to run the application.

## Setup

### 1. Install Python
- Download Python from python.org and install it.
- Make sure Python and pip (Python's package manager) are available by running:

```
python --version
pip --version
```

### 2. Unzip the Django Project
- Extract the zipped project into a folder.
- Navigate to the project directory in a terminal.

### 3. Activate Virtual Environment
The project must be loaded in a virtual environment, which defined the package scope.

For Mac/Linux:
`source venv/bin/activate`

For Windows:
`venv\bin\activate`

You should now see a (venv) in front of the folder path in your terminal, indicating you are in the virtual environment.

### 4. Install Dependencies
Now that the virtual environment is running, type:

`pip install -r requirements.txt`

Which will install dependencies.

### 5. Run Server
Once dependencies are installed, type:

`python manage.py runserver`

This will boot up the python-django application in the terminal window. You can then go to http://localhost:8000 to interact with the application.

# Created By: 
- Adam Pachulski
- CST 8002
- Programming Language Project
- Assignment Date: April 17, 2025
- Github Link to project: https://github.com/AdarrFX/pollapp
