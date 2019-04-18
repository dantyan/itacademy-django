# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from forum.models import Thread


class ThreadTest(APITestCase):

    def test__get_list(self):
        print('test__get_list')

        Thread.objects.create(
            title='test title',
            description='test description'
        )

        url = reverse('forum:thread-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        ret = res.json()

        self.assertEqual(len(ret), 1)

        _thread = ret[0]
        self.assertEqual('test title', _thread.get('title'))
        self.assertEqual('test description', _thread.get('description'))

    def test__create(self):
        url = reverse('forum:thread-list')
        res = self.client.post(url, {
            'title': 'test create',
            'description': 'create description',
        }, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        ret = res.json()
        self.assertEqual('test create', ret.get('title'))
        self.assertEqual('create description', ret.get('description'))

    def test__create_retrieve(self):
        # создание форума
        url = reverse('forum:thread-list')
        res = self.client.post(url, {
            'title': 'test create',
            'description': 'create description',
        }, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        ret = res.json()
        print(ret)

        # получение форма
        url = reverse('forum:thread-detail', kwargs={"pk": ret.get('id')})
        print('url', url)
        res = self.client.get(url)
        ret = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(ret)
