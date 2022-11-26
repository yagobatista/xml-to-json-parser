from django.test import TestCase, Client


class XMLConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_document_bad_request(self):
        response = self.client.post('/connected/')
        self.assertEqual(response.status_code, 400)

    def test_invalid_http_method_put(self):
        response = self.client.put('/connected/')
        self.assertEqual(response.status_code, 405)

    def test_invalid_http_method_patch(self):
        response = self.client.patch('/connected/')
        self.assertEqual(response.status_code, 405)

    def test_invalid_http_method_delete(self):
        response = self.client.delete('/connected/')
        self.assertEqual(response.status_code, 405)
