from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status


# enums for asserts
INDEX_TITLE = 0
INDEX_CONTENT = 1

class ItemTestCase(APITestCase):
    posts = [
            ('First Post', 'Hello, World'),
            ('Second Post', 'Howdy, Partner'),
            ('Third Post', 'Holla, Hombre'),
            ('Fourth Post', 'Konichiwa, Kyoudai'),
            ('Fifth Post', 'Ola, Companheiro'),
            ]

    def setUp(self):
        for t, ct in self.posts:
            data = {
                    'username': 'bnishi',
                    'title': t,
                    'content': ct,
                    }
            response = self.client.post('/careers/', data)


    def test_get_items(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_items(self):
        # redundant considering setUp
        data = {
                'username': 'post tester',
                'title': 'some other post',
                'content': 'what a nice post',
                }
        response = self.client.post('/careers/', data)
        self.assertEqual(response.status_code, 201)

    def test_update_item(self):
        post_id = 2
        new_title = 'Another Post'

        # get posts to check if contents changed
        db_data = self.client.get('/careers/').data

        # updates Third Post
        response = self.client.patch(f'/careers/{post_id}', {'title': new_title})
        self.assertEqual(response.status_code, 200)
        data = dict(response.data)
        print(data)

        # response.data is not dict. it is ReturnDict
        self.assertEqual(data['title'], new_title)

        # post_id-1 because db counts from 1
        self.assertEqual(data['content'], db_data[post_id-1]['content'])
        print('success, {} \n {}', data['title'], data['content'])

    def test_delete_item(self):
        post_id = 1
        response = self.client.delete(f'/careers/{post_id}')
        self.assertEqual(response.status_code, 204)

