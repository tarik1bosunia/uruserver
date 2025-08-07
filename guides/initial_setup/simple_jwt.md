## [SIMPLE JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
### Simple JWT can be installed with pip:
```bash
pip install djangorestframework-simplejwt
```

### Project Configuration:
Then, your django project must be configured to use the library. In settings.py, add rest_framework_simplejwt.authentication.JWTAuthentication to the list of authentication classes:
```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```

### If you wish to use localizations/translations, simply add `rest_framework_simplejwt` to `INSTALLED_APPS`.
```bash
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]
```

### [Settings](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)
Some of Simple JWT's behavior can be customized through settings variables in settings.py:
# Django project settings.py
```python
from datetime import timedelta
...
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
```
### ROTATE_REFRESH_TOKENS = True and need BLACKLIST_AFTER_ROTATION = True
| Setting                    | Value  | Why                                                                                      |
| -------------------------- | ------ | ---------------------------------------------------------------------------------------- |
| `ROTATE_REFRESH_TOKENS`    | `True` | Each refresh use generates a **new token**, reducing the risk of token reuse.            |
| `BLACKLIST_AFTER_ROTATION` | `True` | The old refresh token is **invalidated**, preventing replay attacks if it's ever leaked. |
