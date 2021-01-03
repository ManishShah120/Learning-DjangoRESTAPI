# Session Authentication and Permission

## Permission Classes
Permissoin in REST framework are always defined as a list of permission classes
- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- DjangoModelPermissions
- DjangoModelPermissionsOrAnonReadOnly
- DjangoObjectPermissions[Covered till here in this Commit]
- Cusstom Permissions
