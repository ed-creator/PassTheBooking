from django.conf.urls import include, url
from registration.backends.hmac.views import RegistrationView

from .forms import MyCustomUserForm

from . import views

app_name = 'client'
urlpatterns = [
    url(r'^register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^(?P<client_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index')
]
