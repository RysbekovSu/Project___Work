from django.urls import path
from . import views
urlpatterns = [
    path('vacancy/', views.vacancy, name='vacancy'),
    path('add-vacancy/', views.VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/<int:id>/delete/', views.VacancyDelete.as_view(), name='vacancy_delete'),
    path('vacancy/<int:id>/update/', views.VacancyUpdate.as_view(), name='contact_update'),
]