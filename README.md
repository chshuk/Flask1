Demo App for Lesson 4 GeekBrains
Install
Create new virtual env
python3 -m venv ./venv
copy example.env to .env and set SECRET_KEY
activate virtual env
source venv/bin/activate
install dependencies
pip install -r requirements.txt
Run command for init db and create user
flask db upgrade
flask create-init-user
Run flask application
flask run