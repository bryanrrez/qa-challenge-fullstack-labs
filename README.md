# Appointment Managment Automation project

This repository contains an automation project for Appointment Managment app.

To run test cases you will need to install some dependencies, these are Python (version 3.8 or _higher_) and Pipenv.

You can find Python [here](https://www.python.org/downloads/). After you install Python proceed to install Pipenv library that will allow to install the dependencies of the project.

## Setup

After you successfully install Python, proceed to follow these steps:

1. Run `pip install pipenv` command on a terminal or console. This will install the library necessary to install the project's dependencies.
2. Clone this project using __git__. Run the following command `git clone [git repository]`.
3. cd appointment-managment
4. Run `pipenv install`. This will create a virtual envrionment and install all the dependencies of the project.
5. Run `pipenv shell`. This spwans a shell within the virtual environment.

## How to run the test cases?

You will need to run the command `pipenv run pytest`. If you want to generate a report you could use this command instead `pipenv run pytest --html=src/reports/report.html --self-contained-html`.