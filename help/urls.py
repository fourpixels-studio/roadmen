from django.urls import path
from .views import privacy_policy, terms_and_conditions

urlpatterns = [
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("terms-and-conditions/", terms_and_conditions,
         name="terms_and_conditions"),
]
