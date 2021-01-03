# Basic Authentication & Permission

With whih we can do:
- Data is always associated with a creator.
- Only authenticated users may create Data.
- Only the creator of a Data may update or delete it.
- Unathenticatated requests should have full read-only access.

REST framework provides a number of authentication schemes ou of the box, and also allows you to implement custom schecmes.
- BasicAuthentication
- SessionAuthentication
- TookenAuthentication
- RemoteUserAuthentication
- Cutom authentication
