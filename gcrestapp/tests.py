from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from gcrestapp.models import Restaurant

class RestaurantTestCase(APITestCase):

    def test_post_w_auth(self):
        """
        Test that an authenticated user can create a restaurant instance.
        """
        self.username = 'tester'
        self.password = 'password'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/restaurants/', {'owner': 'Tester','name':'Tester Pub'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Tester Pub')

    def test_post_w_o_auth(self):
        """
        Test that an unauthenticated user cannot create a restaurant instance.
        """
        response = self.client.post('/restaurants/', {'owner': 'Tester','name':'Tester Pub'}, format='json')
        self.assertEqual(response.status_code, 401)

    def test_delete_w_auth(self):
        """
        Test that an authenticated user can create a restaurant instance.
        """
        self.username = 'tester'
        self.password = 'password'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        Restaurant.objects.create(owner='New Owner', name='Pizza')
        response = self.client.delete('/restaurants/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Restaurant.objects.count(), 0)

    def test_delete_w_o_auth(self):
        """
        Test that an unauthenticated user cannot create a restaurant instance.
        """
        Restaurant.objects.create(owner='New Owner', name='Pizza')
        response = self.client.delete('/restaurants/1/')
        self.assertEqual(response.status_code, 401)


    def test_list(self):
        """
        Test the List API for a single restaurant instance.
        """
        Restaurant.objects.create(owner='New Owner', name='Pizza')
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.content, b'[{"id":1,"owner":"New Owner","name":"Pizza","website":null,"street":null,"city":null,"state":null,"zip":null}]')

    def test_detail(self):
        """
        Test the Detail API to return the correct instance.
        """
        Restaurant.objects.create(owner='New Owner', name='Pizza')
        response = self.client.get('/restaurants/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"id":1,"owner":"New Owner","name":"Pizza","website":null,"street":null,"city":null,"state":null,"zip":null}')

    def test_missing_detail(self):
        """
        Test the Detail API to return the correct instance.
        """
        Restaurant.objects.create(owner='New Owner', name='Pizza')
        response = self.client.get('/restaurants/2/')
        self.assertEqual(response.status_code, 404)
