# Openclassrooms Project 12

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## To start

### Requirements

- Python 3
- PostgreSQL

### Installation

- Clone or download this repository, extract it inside a folder if necessary, then open a command prompt inside this folder.

- In the command prompt, create a new environment for the python project :

##### (You need the venv package from PiP to do it, if you don't have it, please write `pip install venv` to install it)

To create a new environment, write this command :

`virtualenv env`

Then you need to activate it :

### Windows :

```bash
cd env/Scripts

activate

cd ../..
```

### Linux/Mac Os:

```bash
source env/Scripts/activate
```

And finally, you can install the required packages for the project :

`pip install -r requirements.txt`

## Usage

Inside the project folder run the following commands :

`py epicevents/manage.py runserver`

## Endpoints

```
/api-token-auth/ => Get a JWT Token to login #POST
/clients/ => Get a list of clients or create a new one #GET #POST
/clients/{client_id} => Get/Update infos of a specific client or delete him #GET #PUT #DELETE
/clients/{client_id}/contracts/ => Create a new contract for this client #POST
/contracts/ => Get a list of contracts #GET
/contracts/{contract_id} => Get/Update infos of a specific contract or delete it #GET #PUT #DELETE
/contracts/{contract_id}/events => Create a new event for this contract #POST
/events/ => Get a list of events #GET
/events/{event_id} => Get/Update infos of a specific event or delete it #GET #PUT #DELETE
```


## Built with

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest](https://www.django-rest-framework.org/)