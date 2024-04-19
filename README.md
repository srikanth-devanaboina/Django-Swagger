# Swagger Integration Guide for Django

This guide details the setup required to integrate Swagger documentation using `drf-yasg` into a Django application for the AWARE platform. It covers the necessary packages, configuration settings, and URL setup.

## Requirements

First, ensure that you have the following packages installed in your Django environment:

```
drf-yasg==1.20.0
```

You can install these using pip:

```bash
pip install drf-yasg==1.20.0
```

## Django Settings Configuration

### Update `INSTALLED_APPS`

Add `drf_yasg` to the `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'drf_yasg',
    ...
]
```

### Swagger Settings

Configure the Swagger settings in your `settings.py` as follows:

```python
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "Auth Token eg [Bearer (JWT) ]": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        },
        'Accept-Language': {
            "type": "apiKey",
            "name": "Accept-Language",
            "in": "header"
        }
    },
}
```

## URLs Setup in Django

### Modify `urls.py`

In your main Django app (e.g., `main_app/urls.py`), set up the URLs for Swagger and ReDoc documentation interfaces. Here's how to do it:

```python
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    """Generate schema for both HTTP and HTTPS."""
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

schema_view = get_schema_view(
    openapi.Info(
        title="Title of your application",
        default_version="v1",
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
```

![Screenshot from 2024-04-19 14-55-39](https://github.com/srikanth-devanaboina/Django-Swagger/assets/82710582/2192fb8c-e719-4432-a733-bed70e434fea)



## Summary

The above settings and configurations enable your Django application to serve API documentation using both Swagger UI and ReDoc. This documentation is accessible over both HTTP and HTTPS protocols and includes security definitions for API key and Accept-Language headers. Ensure you have properly configured the CORS headers if your API is accessed from different domains.

