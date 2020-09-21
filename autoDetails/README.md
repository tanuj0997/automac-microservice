# AutoDetails(Service 1)
###### Notes: To check the functionality of both the services setup and run both the services and create the users from the second service(user manager) and create data from manufracture and car using first service. now try to login on first service using the cred that was setup through the first service. 
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
```CREATE DATABASE auth_manufac;
CREATE USER developer WITH PASSWORD 'developer';
ALTER ROLE developer SET client_encoding TO 'utf8';
ALTER ROLE developer SET default_transaction_isolation TO 'read committed';
ALTER ROLE developer SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE auth_manufac TO developer;
```

### Follow below setups to setup the application.
- Create the virtual envoirments with python 3.6 version and activate
    sh
    $ virtualenv --python=python3.6 env
    $ source env/bin/activate
    
- Install python  dependencies, run into the project root directory.
	sh
    $ pip install -r requirements.txt
    

- Go the the auto details directory and run the script.
    sh
    $ python manage.py migrate
    $ python manage.py assign_user_group_permissions
    $ python manage.py runserver
  
# API ENDPOINTS
#### Manufacturer(Need Admin Privileges)
1. Admin Panel to view car and manufacturer.
    ```sh
    http://localhost:8000/admin/
    ```
2. Create manufacturer HTTP method: POST.
    ```sh
    http://localhost:8000/api/v1/manufacturers/
    ```
3. Update manufacturer HTTP method: PATCH.
    ```sh
    http://localhost:8000/api/v1/manufacturers/id/
    ```
4. Delete manufacturer HTTP method: DELETE.
    ```sh
    http://localhost:8000/api/v1/manufacturers/id/
    ```
5. Get manufacturer HTTP method: GET(Allow any user).
    ```sh
    http://localhost:8000/api/v1/manufacturers/id/
    http://localhost:8000/api/v1/manufacturers/
    ```
#### Cars(Need Admin Privileges)
1. Admin Panel to view car and manufacturer.
    ```sh
    http://localhost:8000/admin/
    ```
2. Create car details HTTP method: POST.
    ```sh
    http://localhost:8000/api/v1/cars/
    ```
3. Update car details HTTP method: PATCH.
    ```sh
    http://localhost:8000/api/v1/cars/id/
    ```
4. Delete car details HTTP method: DELETE.
    ```sh
    http://localhost:8000/api/v1/cars/id/
    ```
5. Get car details HTTP method: GET(Allow any user).
    ```sh
    http://localhost:8000/api/v1/cars/id/
    http://localhost:8000/api/v1/cars/
    ```



