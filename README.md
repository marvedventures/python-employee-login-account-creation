# Python Employee Account Creation

This is a Employee Account Creation using map function, list comprehensions, dictionary comprehensions and f strings.

## Table of contents

- [Overview](#overview)
  - [How to use the project](#how-to-use-the-project)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### How to use the project

#### Step 1: Setting up Initial Requirements:

1. Python 3.11 and above — Follow [this link](https://www.python.org/downloads/) to download Python for your operating system. You can refer to these tutorials on YouTube for the same — Windows, Mac-OS, Ubuntu (it’ll be somewhat similar for other Linux distributions).

2. pip — pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.

3. Install pipenv using pip — pip install pipenv

#### Step 2: Setting up Python Virtual Environment using pipenv:

1. Install required dependencies using pipenv — pipenv install
2. Activate Python Virtual Environment — pipenv shell
3. Run the program — python main.py

### Screenshot
![image](https://user-images.githubusercontent.com/108392678/236618483-987e7ebe-a2bf-428c-9eda-db30cf1965fd.png)


### Links

- Github: [Code](https://github.com/marvedventures/python-employee-login-account-creation)

## My process

### Built with

- [Python](https://www.python.org/) - python.org
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Python Virtual Environment.

### What I learned

- Python Functions
- Python Map function
- Python List Comprehensions
- Python Dictionary Comprehensions
- Python Data Structures
- Python F strings

Here is a code snippet:

```py
# Input data: List of dictionaries
employee_list = [
    {'id': 12345, 'name': 'John', 'department': 'Kitchen'},
    {'id': 12456, 'name': 'Paul', 'department': 'House Floor'},
    {'id': 12478, 'name': 'Sarah', 'department': 'Management'},
    {'id': 12434, 'name': 'Lisa', 'department': 'Cold Storage'},
    {'id': 12483, 'name': 'Ryan', 'department': 'Inventory Mgmt'},
    {'id': 12419, 'name': 'Gill', 'department': 'Cashier'}
]


# Function to be passed to the map() function.
def mod(employee_list):
    temp = employee_list['name'] + '_' + employee_list['department']
    return temp


# Modifies the employee list of dictionaries into list of employee_department strings
def to_mod_list(employee_list):
    return list(map(mod, employee_list))


# Generates a list of usernames
def generate_usernames(mod_list):
    return [el.replace(' ', '_') for el in mod_list]


# Maps employee id to first 4 letters of name
def map_id_to_initial(employee_list):
    return {el['id']: el['name'][:4] for el in employee_list}
```

### Useful resources

- [Map Function in Python](https://www.geeksforgeeks.org/python-map-function/) - This helped me use python map function.
- [Python Comprehensions](https://www.geeksforgeeks.org/comprehensions-in-python/) - This helped me understand the use of python comprehensions.
- [Pipenv Setup](https://python.plainenglish.io/setting-up-a-basic-django-project-with-pipenv-7c58fa2ec631) - This helped me setup my python virtual env

## Author

- Website - [Marvin Morales Pacis](https://marvin-morales-pacis.vercel.app/)
- LinkedIn - [@marvedventures](https://www.linkedin.com/in/marvedventures/)
- Twitter - [@marvedventures](https://www.twitter.com/marvedventures)
