from django.shortcuts import render
from .models import PrivacyPolicy, TermsAndCondition


def terms_and_conditions(request):
    terms = TermsAndCondition.objects.first()
    code_of_conduct_list = [
        item.strip()
        for item in terms.code_of_conduct.splitlines()
        if item.strip()
    ]
    user_of_services_list = [
        item.strip()
        for item in terms.user_of_services.splitlines()
        if item.strip()
    ]
    events_participation_list = [
        item.strip()
        for item in terms.events_participation.splitlines()
        if item.strip()
    ]
    limitation_liability_details_list = [
        item.strip()
        for item in terms.limitation_liability_details.splitlines()
        if item.strip()
    ]

    context = {
        "terms": terms,
        "title_tag": "Terms And Conditions",
        "code_of_conduct_list": code_of_conduct_list,
        "user_of_services_list": user_of_services_list,
        "events_participation_list": events_participation_list,
        "limitation_liability_details_list": limitation_liability_details_list,
        "seo_description": "By accessing or using our website, membership program, or services, you agree to comply with the following terms and conditions.",
    }
    return render(request, 'terms_and_conditions.html', context)


def privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.first()
    collected_info_list = [
        item.strip()
        for item in privacy_policy.information_we_collect.splitlines()
        if item.strip()
    ]
    how_info_is_used_list = [
        item.strip()
        for item in privacy_policy.how_we_use_your_information.splitlines()
        if item.strip()
    ]
    sharing_info_list = [
        item.strip()
        for item in privacy_policy.sharing_of_information.splitlines()
        if item.strip()
    ]
    your_rights_list = [
        item.strip()
        for item in privacy_policy.your_rights.splitlines()
        if item.strip()
    ]

    context = {
        "title_tag": "Privacy Policy",
        "privacy_policy": privacy_policy,
        "your_rights_list": your_rights_list,
        "sharing_info_list": sharing_info_list,
        "collected_info_list": collected_info_list,
        "how_info_is_used_list": how_info_is_used_list,
        "seo_description": "This Privacy Policy outlines how we collect, use, and protect your personal information when you engage with our website, membership program, and related activities."
    }
    return render(request, 'privacy_policy.html', context)
