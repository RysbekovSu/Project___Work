from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main_all, name='main'),

    path('aboutInai/<int:id>/update/', views.AboutInaiUpdate.as_view(), name='main'),

    path('main/<int:id>/update/', views.PopularUpdate.as_view(), name='main'),
    path('main/<int:id>/delete/', views.PopularDelete.as_view(), name='main'),
    path('add-popular/', views.PopularCreate.as_view(), name='add-popular'),


    path('add-contact/', views.ContactCreate.as_view(), name='contact_create'),
    path('contact/<int:id>/delete/', views.ContactDelete.as_view(), name='contact_delete'),
    path('contact/<int:id>/update/', views.ContactUpdate.as_view(), name='contact_update'),

    path('stats/<int:id>/update/', views.StatsUpdate.as_view(), name='contact_update'),
]