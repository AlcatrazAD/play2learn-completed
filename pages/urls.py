from django.urls import path

from .views import AboutView, HomePageView, ContactView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
]