from django.urls import path

from .views import ContactView, ContactThankView

app_name = 'jobs'
urlpatterns = [
    path('contacted-app/', ContactView.as_view(), name='contact'),
    path('contacted-app/thanks/', ContactThankView.as_view(), name='thanks'),
]