from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', home, name='home'),  # home page public website
    path('about-us/', about_us, name='about_us'),  # about us public page
]
