from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from Api.models import Book
import json

http = 'http://127.0.0.1:8080'
data = {"id": 1, "title": "test", "description": "test", "author": "test"}
dataUpdate = {"id": 1, "title": "tested", "description": "tested", "author": "tested"}

# Create your tests here.
class Test(APITestCase):

    def test200(self):
        client = RequestsClient()
        response = client.get(http)
        assert response.status_code == 200

    """
        Test Get
    """

    def testGet200(self):
        client = RequestsClient()
        response = client.get(http+'/api/')
        assert response.status_code == 200

    def testGetLength(self):
        self.client.get((http + '/api/'))
        assert Book.objects.count() <= 0

    """
        Test Post
    """

    def testPost201(self):
        client = RequestsClient()
        response = client.post(http+'/api/', json.dumps(data))
        assert response.status_code == status.HTTP_201_CREATED

    def testPostLength(self):
        self.client.post(http+'/api/', data, format='json')
        assert Book.objects.count() == 1

    def testPostContent(self):
        self.client.post(http+'/api/', data, format='json')
        assert Book.objects.get().title == 'test'
        assert Book.objects.get().description == 'test'
        assert Book.objects.get().author != 'Charles'

    """
        Test Delete
    """

    def testDelete204(self):
        self.client.post(http + '/api/', data, format='json')
        client = RequestsClient()
        response = client.delete(http + '/api/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def testDeleteLength(self):
        self.client.post(http + '/api/', data, format='json')
        self.client.post(http + '/api/', data, format='json')
        assert Book.objects.count() == 2
        self.client.delete((http + '/api/'))
        assert Book.objects.count() == 0

    """
        Test Get ID
    """

    def testGetId200(self):
        self.client.post(http + '/api/', data, format='json')
        client = RequestsClient()
        response = client.get(http+'/api/1')
        assert response.status_code == status.HTTP_200_OK

    def testGetId400(self):
        client = RequestsClient()
        response = client.get(http+'/api/1')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def testGetIdContent(self):
        self.client.post(http + '/api/', data, format='json')
        client = RequestsClient()
        response = client.get(http + '/api/1')
        assert response.json() == data

    """
            Test Put
    """

    def testPut200(self):
        self.client.post(http + '/api/', data, format='json')
        client = RequestsClient()
        response = client.put(http + '/api/1', json.dumps(dataUpdate))
        assert response.status_code == status.HTTP_200_OK

    def testPutLength(self):
        self.client.post(http + '/api/', data, format='json')
        self.client.put(http + '/api/1', dataUpdate, format='json')
        assert Book.objects.count() == 1

    def testPutContent(self):
        self.client.post(http + '/api/', data, format='json')
        self.client.put(http + '/api/1', dataUpdate, format='json')
        assert Book.objects.get().title == 'tested'
        assert Book.objects.get().description == 'tested'
        assert Book.objects.get().author != 'Charles'

    """
        Test Delete
    """

    def testDeleteID204(self):
        self.client.post(http + '/api/', data, format='json')
        client = RequestsClient()
        response = client.delete(http + '/api/1')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def testDeleteLength(self):
        self.client.post(http + '/api/', data, format='json')
        self.client.post(http + '/api/', data, format='json')
        assert Book.objects.count() == 2
        self.client.delete((http + '/api/1'))
        assert Book.objects.count() == 1
