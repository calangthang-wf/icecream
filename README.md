# ICECREAM
* Social Network webapp
* This project uses python django and mysql
* _! This project is not completed yet_

***

# Contact for work
* **Telegram:** [calangthang](https://t.me/it_is_daijobu)
* **Email:** calangthangxc9n@gmail.com

***

# **SET UP**

## **Install Python**
1. Visit offical website: https://www.python.org/downloads/
2. Download Python 3.x (Recommend: 3.9).
3. Install.

## **Install Package**
1. `pip install -r requirements.txt`

## **Install Mysql**
1. Visit offical website: https://dev.mysql.com/downloads/installer/
2. Install another library to use the MySQL database: 
`pip install mysqlclient`.

## **Connect Mysql to Django**
1. Open Mysql cmd.
2. Use the `create database my_database` query. It will create the new database.
3. Update the settings.py
*   `DATABASES = {  
        'default': {  
            'ENGINE': 'django.db.backends.mysql',  
            'NAME': 'my_database',  
            'USER': 'root',  
            'PASSWORD': 'your_password',  
            'HOST': '127.0.0.1',  
            'PORT': '3306',  
            'OPTIONS': {  
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
            }  
        }  
}  `
4. Run the migrate command
`python manage.py migrate`
* **Read more: https://www.javatpoint.com/how-to-connect-mysql-to-django**

# **RUN PROJECT**
* `python manage.py runserver`
