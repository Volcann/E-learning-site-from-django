## **WEEK TWO TASK: E-learning Site Development**  
- Note: Without Django Rest Framework.

### Version 1: Key Deliverables  
- **Basic Structure:** Commit the project to GitHub.  
- **Authentication System:** Enable Signup, Login, and Logout functionality.  

### Models & CRUD Operations  
1. **Models:** Create `Course` and `Lecture` models.  
2. **CRUD:** Implement Create, Read, Update, Delete views and templates with `forms.py`.

---

## **WEEK THREE TASK: API Development with Django Rest Framework**

### Key Updates  
- **Added DRF (Django Rest Framework):** Implemented API endpoints to handle CRUD operations and user authentication.
- **Authentication:** Replaced OAuth with JWT tokens for improved authentication.  
- **Debugging & Performance Optimization:** Added `debug_toolbar` for debugging and optimized database queries. Response time was reduced from 12ms to 3ms-7ms using `prefetch_related` and `select_related`.
- **Updated Permissions:** 
  - Only course creators can modify course content.
  - Other users can only view or add new courses.
- **API Testing:** Tested the API using Chrome Extension Mod Header for JWT authentication.
- **Unit Testing:** Currently working on unit tests for the API.

---

### Reference  
- **Guide:** [Django Documentation PDF](https://github.com/Volcann/E-learning-site-from-django/blob/13c3c4b87b3ff7452d754ecfcb9406a65a432e21/Django%20Training%20Manual.pdf)

*Embed the PDF in your browser to view directly.* 
