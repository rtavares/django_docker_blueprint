## Base skeleton project for Django  

Using:
- Docker / docker-compose
- Gunicorn
- dotenv for control dev/prod environment
- Already a basic 'main' app in place
- Utility scripts

### How to use
- Update project name 'project' to the name of your project where required.  
- Run as needed:
    - `docker-compose up --build -d` 
    - `docker-compose up -d` 
    - `docker-compose stop` 
    - `scripts/restart_project.sh`
    - To run Django 'manage.py' commands:
        - ` docker-compose run project python3 project/manage.py {command}` 
 
