# API Development with Django Rest Framework (DRF)

This project involves the development of a RESTful API using Django Rest Framework (DRF). The API supports CRUD operations, user authentication, and role-based permissions. Below is an overview of the workflow, key updates, and features implemented.

---

## Key Features

1. **CRUD Operations**:  
   Implemented API endpoints to handle Create, Read, Update, and Delete operations for resources.

2. **Authentication**:  
   Replaced OAuth with JWT (JSON Web Tokens) for secure and efficient user authentication.

3. **Permissions**:  
   - Only course creators can modify course content.  
   - Other users can only view or add new courses.

4. **Debugging & Performance Optimization**:  
   - Integrated Django Debug Toolbar for debugging.  
   - Optimized database queries using `prefetch_related` and `select_related`, reducing response time from 12ms to 3ms-7ms.

5. **API Testing**:  
   Tested API endpoints using the Chrome Extension Mod Header for JWT authentication.

6. **Unit Testing**:  
   Currently working on writing unit tests for the API to ensure reliability and functionality.

---

## Workflow

### 1. **Setting Up DRF**
   - Installed Django Rest Framework and configured it in the Django project.
   - Created serializers, views, and URLs for API endpoints.

### 2. **Authentication with JWT**
   - Integrated `djangorestframework-simplejwt` for JWT-based authentication.
   - Configured token generation and refresh endpoints.

### 3. **Permissions**
   - Implemented custom permissions to restrict access:
     - Only course creators can update or delete course content.
     - Other users can only view or create new courses.

### 4. **Debugging & Performance Optimization**
   - Added Django Debug Toolbar for real-time debugging.
   - Optimized database queries using `prefetch_related` and `select_related` to reduce response time.

### 5. **API Testing**
   - Used Mod Header Chrome Extension to simulate JWT authentication during testing.
   - Tested all CRUD operations and authentication flows.

### 6. **Unit Testing**
   - Currently developing unit tests using Django's testing framework to ensure API functionality and edge cases are covered.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Volcann/E-learning-site-from-django.git
   cd your-repo-name
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication
- **Token Obtain Pair**: `POST /api/token/`
- **Token Refresh**: `POST /api/token/refresh/`

### Courses
- **List Courses**: `GET /api/courses/`
- **Create Course**: `POST /api/courses/` (Authenticated users only)
- **Retrieve Course**: `GET /api/courses/{id}/`
- **Update Course**: `PUT /api/courses/{id}/` (Course creators only)
- **Delete Course**: `DELETE /api/courses/{id}/` (Course creators only)

---

## Testing

### API Testing
- Use tools like Postman or Mod Header Chrome Extension to test API endpoints with JWT authentication.

### Unit Testing
- Run unit tests using:
  ```bash
  python manage.py test
  ```

---

## Performance Optimization

- Reduced response time from 12ms to 3ms-7ms by optimizing database queries with `prefetch_related` and `select_related`.

---

## Future Work

- Complete unit tests for all API endpoints.
- Implement rate limiting to prevent abuse.
- Add documentation using Swagger or ReDoc.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Acknowledgments

- Django Rest Framework for providing a robust framework for API development.
- `djangorestframework-simplejwt` for JWT authentication support.
- Django Debug Toolbar for debugging assistance.
