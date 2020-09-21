# How to setup the project.
  - python version should be 3.6 or higher
  - Django version 3+
  - Postgressql

### Follow below instruction to install the depedencies.

##### Ubuntu

- Install python3.6
```sh
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.6
    $ sudo apt-get install python3.6-dev
```

- Install Postgres
 ``` 
    $ sudo apt update
    $ sudo apt install postgresql postgresql-contrib
```	
- Install Virtualenv
```
	$ sudo apt-get install python3-pip
	$ sudo pip3 install virtualenv 
```	

##### Mac
- Install python3.6
```sh
	$  brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
    	$  brew switch python 3.6
```

- Install Virtualenv
```sh
	$ sudo easy_install pip
	$ sudo pip install virtualenv
```

## Flow to run auto mac microservices.

1. Go to the autoUsers directory follow the below command:

```
python manage.py migrate
pyhton manage.py createsupseruser
python manage.py runserver 8888
```

2. Go to the autuDetails folder:

```
python manage.py migrate
python manage.py assign_user_group_permissions
python manage.py runserver
```

3. Log in on autuDetails admin panel for authentication using the autoUsers service user creds.

> Note: For APIs end point please check the service README.md file


### Future scope of improvements:
- Unit testcases
- Dockeriaze the project with health checks and graceful shutdown the services
- Logger
