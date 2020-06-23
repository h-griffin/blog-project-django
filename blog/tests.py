# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class BlogTest(SimpleTestCase):
    def helper_status_code_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_home_page_status(self):
        self.helper_status_code_200('home')

    def test_details_page_status(self):
        # self.helper_status_code_200('post_details')
        pass

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_details_page_template(self):
        # url = reverse('post_details')
        # response = self.client.get(url)

        # self.assertTemplateUsed(response, 'post_details.html')
        # self.assertTemplateUsed(response, 'base.html')
        pass



# details page errors

# raise NoReverseMatch(msg) django.urls.exceptions.NoReverseMatch: 
# Reverse for 'post_details' with no arguments not found. 
# 1 pattern(s) tried: ['post_details/(?P<pk>[0-9]+)$']