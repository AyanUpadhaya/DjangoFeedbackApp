# custom urls file
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name="about"),
    path('feedbacks/',views.feedbacks,name="feedbacks")
]