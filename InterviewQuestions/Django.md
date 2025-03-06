
# Django Interview Questions and Answers

## 1. What is Django?  
**Answer:**  
Django is a high-level **Python web framework** that promotes rapid development and clean, pragmatic design. It follows the **MVT (Model-View-Template)** architecture and provides built-in features such as an admin panel, ORM, authentication, and security mechanisms.

## 2. What are the main features of Django?  
**Answer:**  
- **MVT Architecture** (Model-View-Template)  
- **Built-in ORM (Object-Relational Mapping)**  
- **Automatic Admin Interface**  
- **Security Features (CSRF, SQL Injection Protection, XSS, etc.)**  
- **Scalability and Reusability**  
- **Middleware Support**  
- **Built-in Authentication and Authorization**  
- **Support for Caching and REST APIs (via Django REST Framework)**  

## 3. Explain the Django MVT (Model-View-Template) architecture.  
**Answer:**  
- **Model (M):** Represents the database structure and handles data logic.  
- **View (V):** Handles business logic and communicates with the model and template.  
- **Template (T):** Defines the UI/HTML presentation of data.  
Django’s MVT is similar to MVC, but the **framework manages the controller part automatically**.

## 4. What is Django ORM? How does it work?  
**Answer:**  
Django's **Object-Relational Mapping (ORM)** allows developers to interact with the database using **Python code** instead of raw SQL. It automatically converts database tables into Python classes and provides methods for **querying, inserting, updating, and deleting data**.

Example:  
```python
from myapp.models import Student
students = Student.objects.filter(age__gt=18)  # Retrieves students older than 18
```

## 5. What are Django models?  
**Answer:**  
Django **models** define the structure of database tables using **Python classes**. Each model corresponds to a table in the database.

Example:  
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```
This creates a table `Student` with fields `name`, `age`, and `email`.

## 6. What is the use of migrations in Django?  
**Answer:**  
Migrations are used to track database changes and apply schema modifications without manually writing SQL. Django **auto-generates migration files** when models are created or modified.

Commands:  
```sh
python manage.py makemigrations  # Create migration files
python manage.py migrate         # Apply migrations to the database
```

## 7. What are QuerySets in Django?  
**Answer:**  
A **QuerySet** is a collection of database queries that Django’s ORM uses to retrieve and manipulate data.

Example:  
```python
# Retrieve all records
students = Student.objects.all()

# Filter records where age is greater than 18
adult_students = Student.objects.filter(age__gt=18)

# Get a single object
student = Student.objects.get(id=1)
```

## 8. What is Django Middleware?  
**Answer:**  
Middleware is a framework that **processes requests and responses** globally before they reach the view or after they leave the view.

Example middleware:  
- **AuthenticationMiddleware** – Handles user authentication.  
- **SessionMiddleware** – Manages user sessions.  
- **CsrfViewMiddleware** – Provides CSRF protection.  

Adding custom middleware:  
```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
```
Register middleware in `settings.py`:
```python
MIDDLEWARE = [
    'myapp.middleware.MyMiddleware',
]
```

## 9. What is Django Rest Framework (DRF)?  
**Answer:**  
Django REST Framework (**DRF**) is an extension of Django that helps build **RESTful APIs** with authentication, serialization, and request handling.

Example of a simple DRF API View:  
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Welcome to DRF"})
```

## 10. What is the Django Admin Panel, and how do you enable it?  
**Answer:**  
The **Django Admin Panel** provides a **built-in web interface** to manage database records.  

Enable admin panel:  
1. Add `'django.contrib.admin'` to `INSTALLED_APPS` in `settings.py`.  
2. Run migrations:  
   ```sh
   python manage.py migrate
   ```
3. Create a superuser:  
   ```sh
   python manage.py createsuperuser
   ```
4. Start the server and access `/admin/`.  

---

Here are the **next 10 Django interview questions with clear explanations** in **GitHub README format**:

---

## 11. How do you create a custom user model in Django?  
**Answer:**  
Django allows customization of the user model using `AbstractUser` or `AbstractBaseUser`.  

Example using `AbstractUser`:  
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
```
Register in `settings.py`:  
```python
AUTH_USER_MODEL = 'myapp.CustomUser'
```
Then, run migrations to apply changes.

---

## 12. What are Django signals?  
**Answer:**  
Django **signals** allow decoupled components to communicate by sending notifications when certain actions occur (e.g., after saving an object).  

Example (`post_save` signal):  
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def welcome_message(sender, instance, created, **kwargs):
    if created:
        print(f"Welcome {instance.username}!")
```
Register signals in `apps.py` or a `signals.py` file.

---

## 13. How do you implement authentication and authorization in Django?  
**Answer:**  
Django provides built-in authentication (`django.contrib.auth`).  

### Steps:  
1. Use `User` model for authentication.  
2. Implement login/logout with `django.contrib.auth.authenticate()`.  
3. Use `@login_required` and `@permission_required` for authorization.

Example of login view:  
```python
from django.contrib.auth import authenticate, login

def user_login(request):
    user = authenticate(username='test', password='password')
    if user:
        login(request, user)
```

---

## 14. What are forms in Django? How do they work?  
**Answer:**  
Django **forms** simplify HTML form handling, validation, and processing.  

Example:  
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```
Use in views:  
```python
def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
```

---

## 15. What is CSRF protection in Django? How does it work?  
**Answer:**  
Cross-Site Request Forgery (CSRF) is a security attack where unauthorized commands are submitted on behalf of a user. Django provides **CSRF protection** by default using `CsrfViewMiddleware`.

To enable CSRF protection in templates:  
```html
<form method="post">
    {% csrf_token %}
</form>
```
For API views, disable CSRF using:  
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    return HttpResponse("CSRF Disabled")
```

---

## 16. What is the difference between `get()` and `filter()` in Django QuerySets?  
**Answer:**  
- **`get()`** returns **a single object** or raises an exception if multiple/no records are found.  
- **`filter()`** returns a **QuerySet** (a list of objects), even if only one record exists.

Example:  
```python
# get() raises an error if no user found
user = User.objects.get(username="sathish")

# filter() returns a QuerySet (empty if no record exists)
users = User.objects.filter(username="sathish")
```

---

## 17. How does Django handle static and media files?  
**Answer:**  
- **Static files** (CSS, JavaScript, images) are stored in `STATICFILES_DIRS`.  
- **Media files** (uploads) are stored in `MEDIA_ROOT`.

### Configuration in `settings.py`:  
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"
```
Serve media files in development:  
```sh
python manage.py runserver 8000
```

---

## 18. What is the difference between `ForeignKey`, `OneToOneField`, and `ManyToManyField`?  
**Answer:**  
| Field Type      | Relationship Example |
|----------------|--------------------|
| `ForeignKey`   | One-to-many (e.g., one author, many books) |
| `OneToOneField` | One-to-one (e.g., one profile per user) |
| `ManyToManyField` | Many-to-many (e.g., users and groups) |

Example:  
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # One-to-many
```

---

## 19. How do you deploy a Django application?  
**Answer:**  
### Steps:  
1. **Prepare the project:**  
   ```sh
   pip install -r requirements.txt
   python manage.py collectstatic
   ```
2. **Use Gunicorn for serving Django:**  
   ```sh
   gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
   ```
3. **Use Nginx as a reverse proxy (for production).**  
4. **Set up a PostgreSQL database.**  
5. **Use a cloud service like AWS, DigitalOcean, or Heroku.**  

---

## 20. How can you optimize database queries in Django?  
**Answer:**  
### Best Practices:  
1. **Use `select_related()`** for foreign keys (reduces queries).  
2. **Use `prefetch_related()`** for many-to-many fields.  
3. **Avoid looping over QuerySets (`N+1 problem`).**  
4. **Use `values()` or `only()` to fetch specific fields.**  
5. **Use database indexing for faster lookups.**  

Example:  
```python
# Optimized query
books = Book.objects.select_related('author').all()
```

---

# Django Interview Questions and Answers (Part 3)

## 21. What is Django middleware? How does it work?  
**Answer:**  
Django **middleware** is a framework that processes requests and responses globally before reaching views or templates.

Example of custom middleware:  
```python
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware before view")
        response = self.get_response(request)
        print("Middleware after view")
        return response
```
Register in `settings.py`:  
```python
MIDDLEWARE = [
    'myapp.middleware.CustomMiddleware',
]
```

---

## 22. What is the difference between `@login_required` and `@permission_required` decorators?  
**Answer:**  
- **`@login_required`** ensures that only authenticated users access a view.  
- **`@permission_required`** ensures that a user has specific permissions.

Example:  
```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def dashboard(request):
    return HttpResponse("Welcome, User!")

@permission_required('app.view_dashboard', raise_exception=True)
def admin_dashboard(request):
    return HttpResponse("Welcome, Admin!")
```

---

## 23. How does Django handle file uploads?  
**Answer:**  
Django stores uploaded files in `MEDIA_ROOT` and provides a **FileField** or **ImageField**.

### Steps:  
1. Add `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`:  
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```
2. Create a model with `FileField`:  
   ```python
   class Document(models.Model):
       file = models.FileField(upload_to='documents/')
   ```
3. Handle file upload in views:  
   ```python
   def upload_file(request):
       if request.method == "POST":
           file = request.FILES["file"]
           Document.objects.create(file=file)
   ```

---

## 24. How does Django manage database migrations?  
**Answer:**  
Django uses **migrations** to track model changes.  

- Create a migration:  
  ```sh
  python manage.py makemigrations
  ```
- Apply migrations:  
  ```sh
  python manage.py migrate
  ```
- View migration history:  
  ```sh
  python manage.py showmigrations
  ```

---

## 25. What is Django REST framework (DRF)?  
**Answer:**  
Django REST framework (DRF) is a toolkit for building RESTful APIs in Django.

### Key Features:  
- Serialization (`ModelSerializer`)  
- Authentication & permissions  
- API views (`APIView`, `ViewSet`)  

Example API view:  
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Django REST Framework!"})
```

---

## 26. How do you implement pagination in Django?  
**Answer:**  
Django provides a built-in **Paginator** class.

Example:  
```python
from django.core.paginator import Paginator
from django.shortcuts import render
from myapp.models import Product

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})
```

---

## 27. What is Django caching, and how can you enable it?  
**Answer:**  
Django caching improves performance by storing frequently accessed data.  

Enable file-based caching in `settings.py`:  
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
```
Use caching in views:  
```python
from django.core.cache import cache

def my_view(request):
    data = cache.get('my_data')
    if not data:
        data = "Expensive Query Result"
        cache.set('my_data', data, timeout=60)  # Cache for 60 seconds
    return HttpResponse(data)
```

---

## 28. How does Django handle sessions?  
**Answer:**  
Django **sessions** store user data across requests using cookies or databases.

Enable session storage in `settings.py`:  
```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database-backed sessions
```
Set and retrieve session data:  
```python
def set_session(request):
    request.session['username'] = 'Sathish'
    return HttpResponse("Session Set!")

def get_session(request):
    username = request.session.get('username', 'Guest')
    return HttpResponse(f"Hello, {username}!")
```

---

## 29. What is Celery, and how is it used with Django?  
**Answer:**  
Celery is an asynchronous task queue for handling background jobs in Django.

### Steps to integrate Celery:  
1. Install Celery:  
   ```sh
   pip install celery
   ```
2. Configure Celery in Django (`celery.py`):  
   ```python
   from celery import Celery

   app = Celery('myapp', broker='redis://localhost:6379/0')
   ```
3. Create a task:  
   ```python
   @app.task
   def add(x, y):
       return x + y
   ```
4. Run Celery:  
   ```sh
   celery -A myapp worker --loglevel=info
   ```

---

## 30. How can you create a Django API using Django REST Framework (DRF)?  
**Answer:**  
### Steps to create a simple API:  
1. Install Django REST Framework:  
   ```sh
   pip install djangorestframework
   ```
2. Add `rest_framework` to `INSTALLED_APPS`.  
3. Create a serializer:  
   ```python
   from rest_framework import serializers
   from myapp.models import Product

   class ProductSerializer(serializers.ModelSerializer):
       class Meta:
           model = Product
           fields = '__all__'
   ```
4. Create an API view:  
   ```python
   from rest_framework.response import Response
   from rest_framework.views import APIView

   class ProductView(APIView):
       def get(self, request):
           products = Product.objects.all()
           serializer = ProductSerializer(products, many=True)
           return Response(serializer.data)
   ```
5. Add URL patterns:  
   ```python
   from django.urls import path
   from myapp.views import ProductView

   urlpatterns = [
       path('api/products/', ProductView.as_view(), name='product-list'),
   ]
   ```
Now, accessing `/api/products/` will return JSON data.

---

