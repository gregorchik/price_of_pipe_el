from django.urls import path
from .views import SearchPageView

app_name = 'search'

urlpatterns = [
    path('', SearchPageView.as_view(), name='SearchPageView')
]
