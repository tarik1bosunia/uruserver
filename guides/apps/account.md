# Account App 

## installation
```bash
python manage.py startapp account
```
## add `account` app in setting `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    # custom apps
    'account',
]
```
## set `account.User` model as custom user model in django. add the bellow line in django settings. 
```python
AUTH_USER_MODEL = "account.User"
```

## Add Email Configuration in django settings
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
```