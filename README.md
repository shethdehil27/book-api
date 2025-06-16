
## 🚀 Setup Instructions

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

Update `.env` with your own secret key and API keys.

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

## 🗂️ Sample `.env` File Format

```env
DJANGO_SECRET_KEY=your-django-secret-key
DEBUG=True
VALID_API_KEYS=key123,admin456,test789,user000,super999
```

---

## 🔐 API Key Configuration

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

## 🧪 Postman Test Screenshots (5 Valid API Keys)

Below are 5 tests using 5 valid API keys (`key123`, `admin456`, `test789`, `user000`, `super999`):

---

### ✅ 1. Create Book with `key123`

![Create Book with key123](https://github.com/shethdehil27/book-api/blob/main/book_api_SS/Screenshot%202025-06-16%20212414.png?raw=true)

---

### ✅ 2. Create Book with `admin456`

![Create Book with admin456](https://github.com/shethdehil27/book-api/blob/main/book_api_SS/Screenshot%202025-06-16%20212710.png?raw=true)

---

### ✅ 3. Upload Cover with `test789`

![Upload Cover with test789](https://github.com/shethdehil27/book-api/blob/main/book_api_SS/Screenshot%202025-06-16%20213003.png?raw=true)

---

### ✅ 4. Upload Cover with `user000`

![Upload Cover with user000](https://github.com/shethdehil27/book-api/blob/main/book_api_SS/Screenshot%202025-06-16%20213106.png?raw=true)

---

### ✅ 5. Delete Book with `super999`

![Delete Book with super999](https://github.com/shethdehil27/book-api/blob/main/book_api_SS/Screenshot%202025-06-16%20213254.png?raw=true)

---

## 📂 Repository Includes

* ✅ Complete Django project
* ✅ `requirements.txt`
* ✅ `.env.example`
* ✅ `postman_collection.json`
* ✅ Screenshots of Postman tests
* ✅ `README.md` (this file)

---

## 👨‍💻 Author

**Dehil Sheth**
GitHub: [@shethdehil27](https://github.com/shethdehil27)

---
