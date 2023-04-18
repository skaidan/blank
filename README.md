# Manuel Calzado Vidal's Test for Octopus

# Basic structure taken from https://github.com/rephus/django-rest-template and readapted to save time for the real test

## Testing

    docker-compose run todo python manage.py test todo.tests

## Run the server 

    docker-compose up -d

## Run the command

    docker-compose run todo python manage.py readfile <path><file>



## Things to do next 

This is a list of this that should be done before moving to a full environment. 

- Hide passwords
- Build readfile methods
- I will not manage, for now, if a file is not found, command will continue with next file
- I will read the file just line by line, trying to be prepared for stream files or big files.
- Validations for different types of lines y readfile


## Approaching notes:


- My idea is command just read and store data in dabatase. Another asynchronous process would be needed later to validate the data.
- Reads models just expect to store data from files. So we will allow Json fields to store fields related to each type of line. Of course deeper validation would be needed later... but We save time for now.
