import unittest

import app


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.application.config['TESTING'] = True
        app.application.config['WTF_CSRF_ENABLED'] = False
        app.application.config['DEBUG'] = False

        self.app = app.application.test_client()

        self.assertEqual(app.application.debug, False)

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_searchIMDB(self):

        a = app.searchIMDB('ladder', movie=True)
        b = app.searchIMDB('ladder', movie=False)

        self.assertIsNotNone(a)
        self.assertIsNotNone(b)
        self.assertNotEqual(a, b)

    def movie(self):
        return self.app.get(
            '/movie/ladder',
            follow_redirects=True
        )

    def show(self):
        return self.app.get(
            '/show/ladder',
            follow_redirects=True
        )

    def search(self):
        return self.app.get(
            '/search?query=ladder',
            follow_redirects=True
        )

    def test_pages(self):
        response = self.movie()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'movie', response.data)

        response = self.show()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'tv series', response.data)

        response = self.search()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ladder', response.data)


if __name__ == '__main__':
    unittest.main()
