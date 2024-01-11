from App.views import *
from django.urls import path

urlpatterns = [
    path('', PageHome.as_view(), name='all'),
    path('political/', PagePolitical.as_view(), name='political'),
    path('economic/', PageEconomic.as_view(), name='economic'),
    path('sport/', PageSport.as_view(), name='sport'),
    path('cooking/', PageCooking.as_view(), name='cooking'),
    path('nature/', PageNature.as_view(), name='nature'),
    path('construction/', PageConstruction.as_view(), name='construction'),
    path('create/', AddPage.as_view(), name='create'),
    path('<pk>/delete/', DeletePage.as_view(), name='delete'),
    path('<pk>/edit/', EditPage.as_view(), name="edit"),
]