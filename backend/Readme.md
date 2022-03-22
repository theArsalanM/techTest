#EBI Backend Assessment

## Basics
The project consists of a Django application, and a single app within it. It has 3 API endpoints as follows:

```
/api/molecule/ -> List all molecules with pagination
/api/molecule/<pk> -> Details of a single molecule
/api/molecule/<pk>/activity -> Activity details of a single molecule (paginated)
```

Molecule app is structured to have a single Views.py file, and whole implementation covered in a single ViewSet.

## Test Cases
Since we got a legacy database with some sample data for this assignment, and also because all the APIs are read-only, so I used the same database for testing as well. In order to configure same database for testing, I have written a custom Test Runner at backend.test_runner.py that does not setup a new database or tear down the database after tests are done.

```
DATABASES = {
    'default': {
        ...
        'TEST_NAME': BASE_DIR / 'database.db',
    }
}

TEST_RUNNER = 'backend.test_runner.CustomRunner'
```

Some basic tests can be found in tests.py file. The project has 86% coverage 

``coverage run --source='.' --omit='*/migrations/*.py' manage.py test molecule``

## Docker
The whole project is closed in a Docker container with Python3.9