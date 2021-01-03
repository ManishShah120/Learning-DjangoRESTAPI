# Token Authentication

We learned here how to use the created token using `httpie` and make the use oof the token and perform the belowe operations.

For <> request with Token:-

GET
```http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 8d9f23b860476db289e2779dd42b36e2f24887ac'```

POST
```http -f POST http://127.0.0.1:8000/studentapi/ name=JAY roll=104 city=Dhanbad 'Authorization:Token 8d9f23b860476db289e2779dd42b36e2f24887ac'```

PUT
```http PUT http://127.0.0.1:8000/studentapi/4/ name=JAYChanged roll=105 city=Dhadfdfnbad 'Authorization:Token 8d9f23b860476db289e2779dd42b36e2f24887ac'```

DELETE
```http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Token 8d9f23b860476db289e2779dd42b36e2f24887ac'```
