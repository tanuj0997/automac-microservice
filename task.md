### Create a micro-service project with the following :

1. A Django service that will expose an API that will enable us to create retrieve modify and delete `cars` and 'manufacturers`.
    The cars have 'color', 'number of doors', a list of 'extras' (whatever you like)  an `owner` and a `manufacturer`.
    The manufacturers have a `name` and a `country`, the country is represented by a coutry code and name (fixed number of  10 country code - name pairs ,whichever you want) .

2. A Django second service which serves as a user manager. The user has all the defaults and NOT a `username`. the primary identifier is his email.

3. Details about the authentication and the exposed APIs:
The first service is using the `Users` of the SECOND service as owners of the cars (but NOT the administrators). Owners are just an id, since Service 1  ans Service 2 have different DBs.

The users of the second service are ALSO used for authentication on the first service (the first service DOES NOT USE its own (default authentication) users)

All the users can access the administration panel of the first service.
Only the administrators can create update and delete cars and manufacturers in the first service.

All the users can view all the data from the API in the first service. ( When the cars are retrieved the user's id and full name are displayed in the response) 

Only the administrators can create users in the second service.
A staff user can view only his/her info from the second service.

For the API use django-rest-framework.
The DB of choice is PostgreSQL (servie 1 and service 2 have different databases, can be in the save postgres server)