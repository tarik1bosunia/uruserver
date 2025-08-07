# Django cors headers

## installation

```bash
pip install django-cors-headers
```

## add it to your installed apps

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

## You will also need to add a middleware class to listen in on responses

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

## A list of origins that are authorized to make cross-site HTTP requests

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

| Purpose                  | Required?                       | Explanation                                               |
| ------------------------ | ------------------------------- | --------------------------------------------------------- |
| `CORS_ALLOWED_ORIGINS`   | ✅ Yes                           | Allows browser to send cross-origin requests              |
| `CSRF_TRUSTED_ORIGINS`   | ✅ Yes (for cookie/session auth) | Allows POST/PUT/DELETE requests to pass CSRF protection   |
| `CORS_ALLOW_CREDENTIALS` | ✅ If using cookies              | Allows credentials (cookies, auth headers) to be included |

## You Only Need CSRF_TRUSTED_ORIGINS If

| Case                                                                  | Need it? | Example                                       |
| --------------------------------------------------------------------- | -------- | --------------------------------------------- |
| Accessing Django admin **directly** via `localhost:8000/admin/`       | ❌ No     | This is same-origin, CSRF is handled          |
| Sending **POST/PUT/DELETE** requests to Django **from Next.js**       | ✅ Yes    | Example: calling `/admin/login/` via frontend |
| Using Django **SessionAuthentication + frontend on different origin** | ✅ Yes    | To allow CSRF-protected views to work         |

## Optional: allow cookies & session headers

```python
CORS_ALLOW_CREDENTIALS = True
```
