# Building an API test automation framework with Python
https://m3o.com/user

## Purpose
To build own framework based on the knowledge: [Test automation university](https://testautomationu.applitools.com/)

## Setup

```zsh
# Activate venv
souce env/bin/activate
# Install all dependencies in your virtualenv
pip install -r requirements.txt 
```
Paste your API Key inside .env
```zsh
API_KEY = "dasfsd3223sdfsdf23ds"
```

## How to run
```zsh
pytest -v
```
## Implemented test cases
I have named test files based on functionality
<br> **create_test.py** contains the next test cases: </br>
<br>1. *test_new_user_can_be_added*
<br>Steps: 
- Create new user account 
<br> Excepted result: status code = 200</br>
- Read that the user exists
<br> Excepted result: status code = 200, Json response = data sent on step 1 </br>

<br>2. *test_add_user_invalid_data*
<br> Steps: </br>
- Create new user account 
<br> Excepted result: status code = 500 </br>
- Read that the user doesn't exis
<br> Excepted result: status code = 500 </br>

<br>**delete_test.py** contains the next test cases:</br>
<br> 1. *test_new_user_can_be_deleted* 
<br> Steps: </br>
- Create new user account 
<br>Excepted result: status code = 200
- Delete the user
<br> Excepted result: status code = 200
- Read that the user doesn't exis
<br>Excepted result: status code = 200, response end with None

<br>2. *test_not_existed_user_can_not_be_deleted*
<br> Steps: </br>
- Delete not existed user
<br> Excepted result: status code = 400

<br> **update_test.py** contains the next test cases: </br>
<br> 1. test_user_can_be_updated
<br> Steps: </br>
- Update existed user
<br> Excepted result: status code = 200
- Read the user by id/username
<br> Excepted result: status code = 200, updated data is correct
- Update existed user to initial state
<br> Excepted result: status code = 200
- Read the user by id/email
<br>Excepted result: status code = 200, updated data is correct

<br> 2. test_user_can_not_be_updated
<br> Steps: </br>
- Update unexisted user
<br> Excepted result: status code = 500