# flaskservice-skeleton
boilerplate for a RESTful api in flask. Created by Tylar Hoag <https://github.com/magnuschill/>. Assumes that you will use flask as the application framework with webargs/marshmallow for data marshalling and sqlalchemy for a database ORM

##Usage
Copy the contents of this repo into your new project. change all references to the word APPLICATIONNAME to be your application name. Replace filenames and file contents. For example to change the application to be named mycoolapp:
```
find . -type f -not -path "./.git*" -print0 | xargs -0 sed -i '' -e 's/APPLICATIONNAME/mycoolapp/g'
mv APPLICATIONNAME mycoolapp
mv APPLICATIONNAME.ini mycoolapp.ini
mv APPLICATIONNAME.logrotate mycoolapp.logrotate
```
##Provides
- A basic route to a restful endpoint with GET, POST, PUT, PATCH, DELETE wired up with an optional resource identifier
- A basic healthcheck route which just returns 200. Its reccomended you extend this to provide app specific checks
- an error model implemented to the API spec with unit tests
- Example unit test which calls through the flask framework
- Centralized application logger which can be used as a decorator to log function calls
- Error handlers for standard http errors and custom exceptions
- CORS support if the environment is not set to PROD
- ENV based configuration (uses environment variables)
- Context managers for SQLAlchemy sessions
- Pancakes
