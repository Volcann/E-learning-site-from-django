from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Course, Lecture


class CourseViewTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course_data = {
            'title': 'Test Course',
            'description': 'A test course description',
        }

    def test_create_course(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a course
        response = self.client.post('/api/courses/', self.course_data, format='json')
        
        # Check that the response is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.course_data['title'])
        self.assertEqual(response.data['description'], self.course_data['description'])
        self.assertEqual(response.data['created_by'], self.user.id)

    def test_list_courses(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a course
        Course.objects.create(**self.course_data, created_by=self.user)
        
        # List courses
        response = self.client.get('/api/courses/')
        
        # Check that the course is listed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.course_data['title'])

    def test_course_detail(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a course
        course = Course.objects.create(**self.course_data, created_by=self.user)
        
        # Retrieve course details
        response = self.client.get(f'/api/courses/{course.id}/')
        
        # Check that the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], course.title)
        self.assertEqual(response.data['description'], course.description)

    def test_update_course(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a course
        course = Course.objects.create(**self.course_data, created_by=self.user)
        
        # Update the course
        updated_data = {'title': 'Updated Course Title', 'description': 'Updated description'}
        response = self.client.put(f'/api/courses/{course.id}/', updated_data, format='json')
        
        # Check that the course is updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['description'], updated_data['description'])

    def test_delete_course(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a course
        course = Course.objects.create(**self.course_data, created_by=self.user)
        
        # Delete the course
        response = self.client.delete(f'/api/courses/{course.id}/')
        
        # Check that the course is deleted
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


class LectureViewTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='A test course description', created_by=self.user)
        self.lecture_data = {
            'title': 'Test Lecture',
            'content': 'A test lecture content',
            'course': self.course.id,
        }

    def test_create_lecture(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a lecture
        response = self.client.post('/api/lectures/', self.lecture_data, format='json')
        
        # Check that the response is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.lecture_data['title'])
        self.assertEqual(response.data['content'], self.lecture_data['content'])
        self.assertEqual(response.data['course'], self.course.id)

    def test_list_lectures(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a lecture
        Lecture.objects.create(**self.lecture_data)
        
        # List lectures
        response = self.client.get('/api/lectures/')
        
        # Check that the lecture is listed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.lecture_data['title'])

    def test_lecture_detail(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a lecture
        lecture = Lecture.objects.create(**self.lecture_data)
        
        # Retrieve lecture details
        response = self.client.get(f'/api/lectures/{lecture.id}/')
        
        # Check that the response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], lecture.title)
        self.assertEqual(response.data['content'], lecture.content)

    def test_update_lecture(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a lecture
        lecture = Lecture.objects.create(**self.lecture_data)
        
        # Update the lecture
        updated_data = {'title': 'Updated Lecture Title', 'content': 'Updated lecture content'}
        response = self.client.put(f'/api/lectures/{lecture.id}/', updated_data, format='json')
        
        # Check that the lecture is updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['content'], updated_data['content'])

    def test_delete_lecture(self):
        # Authenticate user
        self.client.login(username='testuser', password='password')
        
        # Create a lecture
        lecture = Lecture.objects.create(**self.lecture_data)
        
        # Delete the lecture
        response = self.client.delete(f'/api/lectures/{lecture.id}/')
        
        # Check that the lecture is deleted
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lecture.objects.count(), 0)