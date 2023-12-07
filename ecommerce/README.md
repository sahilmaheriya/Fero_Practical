### Create virtual environment

```
$ python3 -m venv env
```

### Activate virtual environment

```
$ source env/bin/activate
```


### Migration command

```
$ python manage.py makemigrations
$ python manage.py migrate

 Note - if you face dependencies issues after performing migrations the perform migrations on each
 service individually. The order is mentioned below:
	>>> customer
	>>> product      
	>>> order    
```

### Create super admin user

```
$  python manage.py createsuperuser
	>>>  email_address : admin123@gmail.com
	>>>  username : Admin
	>>>  password : Test@123
```

### Run django server

```
$ python3 manage.py runserver
```

