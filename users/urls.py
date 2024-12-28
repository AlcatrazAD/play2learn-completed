from django.urls import path

from .views import MyAccountPageView

from . import views


urlpatterns = [
    path('my_account/', MyAccountPageView.as_view(), name='my_account'),


]