# Ponddy Cookie Agreement
The simple cookie agreement implementation and logging user accepting action.
## Installation
### Normal
Install using pip
```shell-script
pip install ponddy-cookie-agreement
```

Add `cookie_policy` to your `INSTALL_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'cookie_policy',
]
```
Add endpoint on your API root `urlpatterns`

```python
urlpatterns = [
    ...
    path('cookie/policy/', include('cookie_policy.urls')),
]
```

### Use template
Check your `TEMPLATES` setting already have `request` context process in your `context_processors`

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
            ...,
            'django.template.context_processors.request'
            ],
        },
    }
]
```

Add the CSS and JS file and `include` tag in your template what page you want to show the cookie policy agreement
```html
{% load static %}

<head>

<link href="{% static 'cookie_agreement/cookie.css'%}" rel="stylesheet">
<script src="{% static 'cookie_agreement/cookie.js' %}"></script>

</head>

<body>
{% include 'cookie_agreement.html' %}
</body>
```

## Settings

### URLs
#### `COOKIE_POLICY_URL`
#### `PRIVACY_POLICY_URL`
#### `TERM_OF_SERVICE_URL`

### THROTTLE
Setting the restful default throttle rates for throttling the accept cookie policy API
#### `DEFAULT_THROTTLE_RATES`
Example:
```python
REST_FRAMEWORK = {
	'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',
        'anon': '100/day',
    }
}
```
