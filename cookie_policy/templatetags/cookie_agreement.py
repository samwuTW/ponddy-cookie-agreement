from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def get_cookie_policy():
    return getattr(settings, "COOKIE_POLICY_URL", "")


@register.simple_tag
def get_privacy_policy():
    return getattr(settings, "PRIVACY_POLICY_URL", "")


@register.simple_tag
def get_term_of_service():
    return getattr(settings, "TERM_OF_SERVICE_URL", "")
