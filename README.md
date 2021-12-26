# stepik_auto_test_project

## _Stepik final project for auto test course_

## Course link: https://stepik.org/course/575/

Training project for auto testing course

Tools and instruments used in project:
- pytest
- selenium
- page object (pattern)

## To launch review tests with Windows

It is recommended to use virtual environment (venv)

For this you should create new venv

Create directory for venvs 
```sh
mkdir venvs
cd venvs
```
Create new venv
```sh
python -m venv new_env
```
Activate venv
```sh
new_env\Scripts\activate.bat 
```
You should see name of the venv in console
```sh
> new_env\Scripts\activate.bat
(new_env) С:\Users\User\venvs>
```
Install required packages
```sh
pip install -r \path\to\requirements.txt
```
Make sure the path to ```chromedriver.exe``` added to the PATH variable

Start tests
```sh
pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py
```
