from django.urls import path
from .views import predict_spam,home

urlpatterns = [
    path('index', home, name='home'),
    path('email_spam_predict/', predict_spam, name='predict_spam'),
]
