# AutoUsers(Service 2)
# How to setup the project.
  - python version should be 3.6 or higher
  - Django version 3+
  - Postgressql

### Follow below instruction to install the depedencies.

##### Ubuntu

- Install python3.6
	sh
	$ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
	$ sudo apt-get install python3.6
    $ sudo apt-get install python3.6-dev

- Install Postgres
    sh 
    $ sudo apt update
    $ sudo apt install postgresql postgresql-contrib
	
- Install Virtualenv
	sh
	$ sudo apt-get install python3-pip
	$ sudo pip3 install virtualenv 
	

##### Mac
- Install python3.6
	sh
	$  brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
    $  brew switch python 3.6
	

- Install Virtualenv
	sh
	$ sudo easy_install pip
	$ sudo pip install virtualenv

### Create Postgres database
```CREATE DATABASE auto_users;
CREATE USER developer WITH PASSWORD 'developer';
ALTER ROLE developer SET client_encoding TO 'utf8';
ALTER ROLE developer SET default_transaction_isolation TO 'read committed';
ALTER ROLE developer SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE auto_users TO developer;
```

### Follow below setups to setup the application.
- Create the virtual envoirments with python 3.6 version and activate
    sh
    $ virtualenv --python=python3.6 env
    $ source env/bin/activate
    
- Install python  dependencies, run into the project root directory.
	sh
    $ pip install -r requirements.txt
    

- Go the the auto users directory and run the script.
    ```
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver 8888
    
  ```
# API ENDPOINTS
#### Manufacturer(Need Admin Privileges)
1. Admin Panel to view users.
    ```sh
    http://localhost:8888/admin/
    ```
2. Create user record method: POST.
    ```sh
    http://localhost:8888/api/v1/users/
    ```
3. Update user detail HTTP method: PATCH.
    ```sh
    http://localhost:8000/api/v1/users/id/
    ```
4. Delete users HTTP method: DELETE.
    ```sh
    http://localhost:8000/api/v1/users/id/
    ```
5. Login user HTTP: POST.
    ```sh
    http://localhost:8000/api/v1/login/
    ```
6. Logout users HTTP method: POST.
    ```sh
    http://localhost:8000/api/v1/logout/
    ```

