# Usage

## How to run Docker
```
# At first time
$ docker-compose up --build

# After second time
$ docker-compose up
```

## How to verify user registration and authentication by JWT

### (1) Register user
```
# by django shell
$ docker exec -it drf ash
$ python manage.py shell 
>>> from users.models import User
>>> username = "HIGE"
>>> email = "hige@gmail.com"
>>> password = "Sa20190903"
>>> User.objects.create_user(username, email, password)

# by curl
$ curl localhost/api/v1/users/
       -X POST \
       -H "Content-Type: application/json" \
       -d '{"username":"HIGE", "email":"hige@gmail.com", "password": "Ss20190903"}' \
```

### (2) Verify user to send registered user information
```
# access to users' retirive without JWT
$ curl localhost/api/v1/users/me/
>>> {"detail":"Authentication credentials were not provided."}

# publish JWT  
$ curl -X POST localhost/api/v1/auth/jwt/token/ --data 'username=HIGE&password=Ss20190903'
>>> {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3MzY3ODYyNiwianRpIjoiMjU1OTM0NzZhOWM0NDA5ODgzOTc0M2I5MDRiNTliMzAiLCJ1dWlkIjoiNDEyMmIxYjItNWUwNS00MTFhLWE1NTQtODcwMWQ0ZTkyN2FhIn0.P2rD8l1iUxKy8ROeF1xBa3dQb83sRkv4_aKCMAEreI0",
     "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTczNTkyNTI2LCJqdGkiOiJjZDg4NzdkODYxYzk0Y2VkYTFlMjUzZjM3NzY2YjJlMCIsInV1aWQiOiI0MTIyYjFiMi01ZTA1LTQxMWEtYTU1NC04NzAxZDRlOTI3YWEifQ.9Ja91_QvWmUKcgOZmIRN_aIN3JdozpBf6kWwA3bJ7TU"}

# access to users' retirive with JWT
$ curl localhost/api/v1/users/me/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTczNTkyNTI2LCJqdGkiOiJjZDg4NzdkODYxYzk0Y2VkYTFlMjUzZjM3NzY2YjJlMCIsInV1aWQiOiI0MTIyYjFiMi01ZTA1LTQxMWEtYTU1NC04NzAxZDRlOTI3YWEifQ.9Ja91_QvWmUKcgOZmIRN_aIN3JdozpBf6kWwA3bJ7TU'
>>> {"email":"hige@gmail.com","uuid":"ee7fd01e-f21d-49fb-b1ae-256c7d0ed5ff","username":"HIGE"}

# refresh JWT
$ curl -X POST localhost/api/v1/auth/jwt/refresh/ --data 'refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3MzY3ODYyNiwianRpIjoiMjU1OTM0NzZhOWM0NDA5ODgzOTc0M2I5MDRiNTliMzAiLCJ1dWlkIjoiNDEyMmIxYjItNWUwNS00MTFhLWE1NTQtODcwMWQ0ZTkyN2FhIn0.P2rD8l1iUxKy8ROeF1xBa3dQb83sRkv4_aKCMAEreI0'
>>> {"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}
```