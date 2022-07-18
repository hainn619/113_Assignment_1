from audioop import reverse
from urllib import response
from django.test import SimpleTestCase, TestCase


class PageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_ABOUT_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_contain_string(self):
        response = self.client.get("/")
        self.assertContains(response, "Home page")

    def test_about_page_contain_string(self):
        response = self.client.get("/about/")
        self.assertContains(response, "About us")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
