from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_and_profile_created(self):
        resp = self.client.post(reverse('register'), {
            'username': 'tester',
            'email': 't@example.com',
            'password1': 'StrongPassw0rd!',
            'password2': 'StrongPassw0rd!'
        })
        # After registration often redirected to home
        self.assertEqual(resp.status_code, 302)
        user = User.objects.filter(username='tester').first()
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.profile)

    def test_login_logout(self):
        user = User.objects.create_user(username='u1', password='pass12345')
        login = self.client.login(username='u1', password='pass12345')
        self.assertTrue(login)
        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)