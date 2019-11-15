# username = corey
# password = root

# username = testuser
# password = root1234

from django.urls import path
from coreyschafer import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
