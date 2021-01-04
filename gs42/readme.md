# HyperlinkedModel Serializer


TO see the internal code structure
```
>>> from api.serializers import StudentSerializer
>>> serializer = StudentSerializer()
>>> print(repr(serializer))
StudentSerializer():
    id = IntegerField(label='ID', read_only=True)
    url = HyperlinkedIdentityField(view_name='student-detail')
    name = CharField(max_length=50)
    roll = IntegerField()
    city = CharField(max_length=50)
```