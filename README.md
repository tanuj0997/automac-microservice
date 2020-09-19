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


### Future scope of improvements:

- Unit testcases
- Dockeriaze the project with health checks and graceful shutdown the services
- Logger 
