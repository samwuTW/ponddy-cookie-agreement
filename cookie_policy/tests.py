from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from .models import AcceptRecord


User = get_user_model()


class CookiePolicyAgreementTest(TestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.get_or_create(
            email='test@abc.xyz', username='test'
        )[0]

    def test_get_accept_page_will_create_a_new_record(self):
        resp = self.client.get(
            reverse('cookie_policy_accept')
        )
        self.assertEqual(
            resp.status_code,
            204
        )
        self.assertEqual(
            AcceptRecord.objects.all().count(),
            1
        )
        assert self.client.session.get('accepted_cookie_policy')

    def test_loged_user_will_create_a_record_with_user(self):
        self.client.force_login(self.user)
        self.client.get(
            reverse('cookie_policy_accept')
        )
        record = AcceptRecord.objects.last()
        self.assertEqual(
            self.user,
            record.user
        )
        assert self.client.session.get('accepted_cookie_policy')

    def test_throttle(self):
        for _ in range(100):
            self.client.get(
                reverse('cookie_policy_accept')
            )
        resp = self.client.get(
            reverse('cookie_policy_accept')
        )
        self.assertEqual(
            resp.status_code, 429
        )
