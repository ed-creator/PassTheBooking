from registration.forms import RegistrationForm

from .models import Client


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = Client
        fields = '__all__'
