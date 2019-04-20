# Create your tests here.
from unittest.mock import Mock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from forum.models import Thread
from user.models import UserModel


class ThreadTest(APITestCase):

    def setUp(self):
        super().setUp()
        self.user = UserModel.objects.create_user('test-user', 'test@test.com', '123qwe')

    def test__get_list(self):
        print('test__get_list')

        obj = Thread.objects.create(
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

    def test__create_not_login(self):
        url = reverse('forum:thread-list')
        res = self.client.post(url, {
            'title': 'test create',
            'description': 'create description',
        }, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test__create_login(self):
        url = reverse('forum:thread-list')
        self.client.force_authenticate(user=self.user)
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
        self.client.force_authenticate(user=self.user)
        res = self.client.post(url, {
            'title': 'test create',
            'description': 'create description',
        }, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        ret = res.json()

        # получение форма
        url = reverse('forum:thread-detail', kwargs={"pk": ret.get('pk')})
        print('url', url)
        res = self.client.get(url)
        ret = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(ret)

    def test__mock_(self):
        url = reverse('forum:mock')
        print(url)
        mock = Mock(return_value='foo')
        with patch('forum.views.mock.some_func', mock):
            res = self.client.get(url)

        res = self.client.get(url)
        mock.assert_called_with(1)
        self.assertEqual(0, 1)

    def test__mock_request(self):
        url = reverse('forum:mock')

        mock = Mock(return_value='foo')
        with patch('forum.views.mock.some_func', mock):
            res = self.client.get(url)

        mock.assert_called_with(100, 12, 2)

        # self.assertEqual(0,1)
