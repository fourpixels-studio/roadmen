from django.contrib import admin
from .models import FAQ, PrivacyPolicy, TermsAndCondition
admin.site.register(FAQ)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsAndCondition)
