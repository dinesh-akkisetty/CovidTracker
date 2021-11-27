from django.test import TestCase
# from .models import User, SelfAssessment
from .views import register_user, calculate_risk


# Create your tests here.
class UserModuleTestCase(TestCase):

    def test_register_user(self):
        name = "A"
        phoneNo = "1234"
        pinCode = "111"
        user_id = register_user(name, phoneNo, pinCode)
        self.assert_(user_id, 1)
