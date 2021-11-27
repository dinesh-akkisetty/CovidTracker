from django.shortcuts import render
from django.views.generic import CreateView

from .models import User, SelfAssessment


# # Create your views here.
# class RegisterUser(CreateView):
#     model = User

# def create_user(self, request):

def calculate_risk(symptoms, travel_history, contact):
    no_of_symptoms = len(symptoms)
    risk_score = 0
    if no_of_symptoms == 0 and travel_history == False and contact == False:
        risk_score = 5
    elif no_of_symptoms == 1 and (travel_history == True or contact == True):
        risk_score = 50
    elif no_of_symptoms == 2 and (travel_history == True or contact == True):
        risk_score = 75
    elif no_of_symptoms > 2 and (travel_history == True or contact == True):
        risk_score = 95
    return risk_score


def register_user(name, phone_no, pin_code):
    user = User(name=name, phone_no=phone_no, pin_code=pin_code)
    user.save()
    return user.pk





