#  Django Book Catalog API

A RESTful API for managing books with API key-based authentication and cover image upload, built using Django and Django REST Framework.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shethdehil27/book-api.git
cd book-api
```

### 2. Create a Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in your root directory:

```bash
cp .env.example .env
```

Update `.env` with your own secret key and API key.

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

Visit the API:

```
http://127.0.0.1:8000/api/books/
```

---

##  Sample `.env` File Format

```env
DJANGO_SECRET_KEY=your-django-secret-key
DEBUG=True
VALID_API_KEYS=your-secret-api-key
```

---

## API Key Configuration

1. Keys are loaded in `settings.py` using `python-decouple`:

   ```python
   from decouple import config
   VALID_API_KEYS = config('VALID_API_KEYS').split(',')
   ```

2. A custom decorator protects views:

   ```python
   def require_api_key(view_func):
       def wrapper(request, *args, **kwargs):
           api_key = request.headers.get('X-API-Key')
           if api_key not in settings.VALID_API_KEYS:
               return JsonResponse({
                   "error": "INVALID_API_KEY",
                   "message": "Missing or invalid API key"
               }, status=401)
           return view_func(request, *args, **kwargs)
       return wrapper
   ```

3. In Postman or frontend apps, pass this header:

   ```
   X-API-Key: your-secret-api-key
   ```

---

##  Postman Test Screenshots

 Place these images in a `screenshots/` folder and embed or link them.

###  1. Create Book – Valid (200 OK)

*Book created successfully*
 `screenshots/create-book-success.png`

---

###  2. Create Book – Invalid ISBN (400)

*ISBN must be exactly 13 characters*
 `screenshots/invalid-isbn.png`

---

###  3. Upload Cover – Valid Image (200 OK)

*Valid image file uploaded*
 `screenshots/upload-cover-success.png`

---

###  4. Upload Cover – File Too Large (413)

*File size exceeds 2MB*
 `screenshots/upload-too-large.png`

---

###  5. Delete Book – Invalid API Key (401)

*API key is missing or incorrect*
 `screenshots/delete-unauthorized.png`

---

##  Repository Includes

*  Complete Django project
*  `requirements.txt`
*  `.env.example`
*  `postman_collection.json`
*  Screenshots of Postman tests
*  `README.md` (this file)

---

##  Author

**Dehil Sheth**
GitHub: [@shethdehil27](https://github.com/shethdehil27)

