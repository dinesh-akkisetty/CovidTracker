from django.shortcuts import render
from .models import Admin, CovidResult
from ..UserModule.models import User


# Create your views here.
def register_admin(name, phone_no, pin_code):
    admin = Admin(name=name, phoneNumber=phone_no, pinCode=pin_code)
    admin.save()
    return admin.pk


def update_result(user_id, admin_id, result):
    user = User.objects.get(pk=user_id)
    admin_id = Admin.objects.get(pk=admin_id)
    covid_result = CovidResult(user_id, admin_id, result)
    covid_result.save()
    return covid_result.pk