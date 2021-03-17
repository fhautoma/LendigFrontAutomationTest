# LendigFrontAutomationTest

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Run](#run)

## General info
This project is simple search on google search page and validate if one specific word exist in the page.
	
## Technologies
Project is created with:
* Selenium version: 3.141.0
* behave version: 1.2.6
* Python version: 3.9
	
## Setup
To setup this project, create virtualenv and install requirements.txt using pip:

```
Windows: Command Prompt or PowerShell
> pip install viertualenv
> python -m venv <root path>/LendingFrontAutomationTest/env 
> cd <root path>\LendingFrontAutomationTest
> .\env\Scripts\activate
> python -m pip install -r requirements.txt

Mac:

$ pip install virtualenv
$ cd LendingFrontAutomationTest/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run
Run on the CLI or execute with an IDE such as Pycharm or Visual Studio Code
```
CLI:
python .\Launcher\runner.py

IDE:
Navigate until the runner.py file and run it: 
LendingFrontAutomationTest > 
                      Launcher >
                           runner.py
```
