from django.urls import path

from .views import home_view, click_url_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:shortened_part>', click_url_view, name = 'redirect'),
]