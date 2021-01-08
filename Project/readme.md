# CRUD Project

## For accessing the Project:
```
http://127.0.0.1:8000/
```


## For accessing the API
```
http://127.0.0.1:8000/api/crud/
```

### For enabling the Browsable API Interface
Comment out this portion of the code in `Project/Project/settings.py`
```
    # To disable the REST Browsable API
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)
    }
```
