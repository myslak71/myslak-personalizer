
[![pipeline status](https://gitlab.com/myslak/wonderful_myslak_world/badges/master/pipeline.svg)](https://gitlab.com/myslak/wonderful_myslak_world/commits/yml)
[![coverage report](https://gitlab.com/myslak/wonderful_myslak_world/badges/master/coverage.svg)](https://gitlab.com/myslak/wonderful_myslak_world/commits/yml)
![](presentation.gif)

### Installation
___
1. PostgreSQL
    ```
    sudo apt-get update
    sudo apt-get install postgresql
    ```
    Create database and use the myslakdb script either in console or pgAdmin
2. Node.js
    ```
    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
    sudo apt-get install -y nodejs
    sudo npm install -g @angular/cli

    npm install rxjs@6 rxjs-compat@6 --save
    npm install file-saver --save
    npm install @types/file-saver --save
    ```
3. Packages 
    ```
    pip install pipenv
    pipenv install
    ```
    
### Configuration
___
In config.py file change DB parameters to meet your PostgreSQL requirements.

### Execution
___
1. Flask

Inside project root directory type:
```
    flask run
```
2. Angular

Inside frontend directory run:
```angular2
    ng serve
```
