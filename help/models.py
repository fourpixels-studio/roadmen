from django.db import models


class PrivacyPolicy(models.Model):
    page_title = models.CharField(max_length=150, blank=True)
    effective_date = models.DateField(blank=True)
    intro_paragraph = models.TextField(blank=True, null=True)

    information_we_collect_title = models.TextField(blank=True, null=True)
    information_we_collect_intro = models.TextField(blank=True, null=True)
    information_we_collect = models.TextField(blank=True, null=True)

    how_we_use_your_information_title = models.TextField(blank=True, null=True)
    how_we_use_your_information_intro = models.TextField(blank=True, null=True)
    how_we_use_your_information = models.TextField(blank=True, null=True)
    how_we_use_your_information_outro = models.TextField(blank=True, null=True)

    membership_verification_title = models.TextField(blank=True, null=True)
    membership_verification_paragraph = models.TextField(blank=True, null=True)

    payment_and_refund_policy_title = models.TextField(blank=True, null=True)
    payment_and_refund_policy_paragraph = models.TextField(blank=True, null=True)

    data_security_title = models.TextField(blank=True, null=True)
    data_security_paragraph = models.TextField(blank=True, null=True)

    use_of_cookies_and_analytics_title = models.TextField(blank=True, null=True)
    use_of_cookies_and_analytics_paragraph = models.TextField(blank=True, null=True)

    sharing_of_information_title = models.TextField(blank=True, null=True)
    sharing_of_information_intro = models.TextField(blank=True, null=True)
    sharing_of_information = models.TextField(blank=True, null=True)
    sharing_of_information_outro = models.TextField(blank=True, null=True)

    your_rights_title = models.TextField(blank=True, null=True)
    your_rights_intro = models.TextField(blank=True, null=True)
    your_rights = models.TextField(blank=True, null=True)

    contact_us_title = models.TextField(blank=True, null=True)
    contact_us_paragraph = models.TextField(blank=True, null=True)
    contact_us_details = models.TextField(blank=True, null=True)

    seo_thumbnail = models.FileField(
        upload_to="help/", blank=True, null=True,
        help_text="Recommended JPEG dimenstions: 1200*628")
    seo_title_tag = models.CharField(
        max_length=80, blank=True, null=True,
        help_text="Keep the your title around 60 characters and put the keywords you're focusing on first")
    seo_keywords = models.TextField(blank=True, null=True)
    seo_description = models.TextField(
        blank=True, null=True,
        help_text="A short description often serving as a pitch to people who find the website on Google or social media sites.")

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policies"

    def __str__(self):
        return str("Privacy Policy")


class TermsAndCondition(models.Model):
    page_title = models.CharField(max_length=150, blank=True)
    effective_date = models.DateField(blank=True)
    intro_paragraph = models.TextField(blank=True, null=True)

    member_eligibility_title = models.TextField(blank=True, null=True)
    member_eligibility = models.TextField(blank=True, null=True)

    membership_fees_title = models.TextField(blank=True, null=True)
    membership_fees = models.TextField(blank=True, null=True)

    code_of_conduct_title = models.TextField(blank=True, null=True)
    code_of_conduct_intro = models.TextField(blank=True, null=True)
    code_of_conduct = models.TextField(blank=True, null=True)
    code_of_conduct_outro = models.TextField(blank=True, null=True)

    user_of_services_title = models.TextField(blank=True, null=True)
    user_of_services_intro = models.TextField(blank=True, null=True)
    user_of_services = models.TextField(blank=True, null=True)

    payments_refunds_title = models.TextField(blank=True, null=True)
    payments_refunds_paragraph = models.TextField(blank=True, null=True)

    events_participation_title = models.TextField(blank=True, null=True)
    events_participation_intro = models.TextField(blank=True, null=True)
    events_participation = models.TextField(blank=True, null=True)

    intellectual_property_title = models.TextField(blank=True, null=True)
    intellectual_property = models.TextField(blank=True, null=True)

    limitation_liability_title = models.TextField(blank=True, null=True)
    limitation_liability_intro = models.TextField(blank=True, null=True)
    limitation_liability_details = models.TextField(blank=True, null=True)

    updates_to_terms_title = models.TextField(blank=True, null=True)
    updates_to_terms = models.TextField(blank=True, null=True)

    contact_us_title = models.TextField(blank=True, null=True)
    contact_us_paragraph = models.TextField(blank=True, null=True)
    contact_us_details = models.TextField(blank=True, null=True)

    seo_thumbnail = models.FileField(
        upload_to="help/", blank=True, null=True,
        help_text="Recommended JPEG dimenstions: 1200*628")
    seo_title_tag = models.CharField(
        max_length=80, blank=True, null=True,
        help_text="Keep the your title around 60 characters and put the keywords you're focusing on first")
    seo_keywords = models.TextField(blank=True, null=True)
    seo_description = models.TextField(
        blank=True, null=True,
        help_text="A short description often serving as a pitch to people who find the website on Google or social media sites.")

    class Meta:
        verbose_name = "Terms And Condition"
        verbose_name_plural = "Terms And Conditions"

    def __str__(self):
        return str("Terms And Conditions")


class FAQ(models.Model):
    question = models.CharField(max_length=200, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
