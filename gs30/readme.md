# JSON Web Toekn and simple JWT in DRF

Thirdparty Packages:-
- Django OAth Toolkit
- JSON Web Token Authentication[JWT] :heavy_check_mark:
> JSON Web Token is a fairly new standard which can be used for token-based authentication. Unlike the built-in TokenAuthentication scheme, JWT Authentication doesn'tneed to use a database to validate a token.(https://jwt.io/)
- Hawk HTTp Authentication
- HTTP Signature Authentication
- Djoser
- django-rest-auth / dj-rest-auth
- django-rest-framework-social-oauth2
- django-rest-knox
- drfpasswrodless


## JWT
CREATE TOKEN
`http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="super123"`

REFRESH TOKEN[required because it gets expired in 5 min(default)]
`http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwOTgzOTM2MCwianRpIjoiNjEwMTFmYjlmZDJhNDQ3ZTllMzgwY2QxZDZhOTUyNDciLCJ1c2VyX2lkIjoxfQ.79PjfyTeH6MbYgy8rGgPviOHReWx4wjK4Hc6vlMOmh0"`

VERIFY TOKEN
`http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NzUzMjYwLCJqdGkiOiJjZDY2OWVmNjg4ZWI0ZmYyYmJlNmRkNTEwMmJmOWE4OSIsInVzZXJfaWQiOjF9.5ah2KjCX9r68IUJi9UUKwr8-Gh8ztR_aIYBtSkDYJb8"`

GET
`http http://127.0.0.1:8000/studentapi/ 'Autherization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NzU0NDA5LCJqdGkiOiJkNWE5NDA1MjNiNDQ0Y2RkODg0MTA3ZjdhY2RiMDdjZSIsInVzZXJfaWQiOjF9.mpSZ14IQ0IKBK2LHk-ithYP3HT8Y_roxfhB-g-qyHus'`

POST
`http -f POST http://127.0.0.1:8000/studentapi/ name=Raja roll=135 city=BOKARUUU 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NzU0NDA5LCJqdGkiOiJkNWE5NDA1MjNiNDQ0Y2RkODg0MTA3ZjdhY2RiMDdjZSIsInVzZXJfaWQiOjF9.mpSZ14IQ0IKBK2LHk-ithYP3HT8Y_roxfhB-g-qyHus'`

PUT
`http PUT http://127.0.0.1:8000/studentapi/3/ name=Rdfaja roll=135 city=BOKfdARUUU 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NzU0NzMzLCJqdGkiOiI5Y2M0ZDg4NWNmODg0MmVmOWE5Y2IzYTNlNDhlMTFiZCIsInVzZXJfaWQiOjF9.PyjyrL86w8L6bvWqDwEDnLO3YxPeVrhhLyxz5y42w4M'`

DELETE
`http DELETE http://127.0.0.1:8000/studentapi/3/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NzU0NzMzLCJqdGkiOiI5Y2M0ZDg4NWNmODg0MmVmOWE5Y2IzYTNlNDhlMTFiZCIsInVzZXJfaWQiOjF9.PyjyrL86w8L6bvWqDwEDnLO3YxPeVrhhLyxz5y42w4M'`
