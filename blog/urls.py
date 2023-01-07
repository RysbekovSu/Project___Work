from django.urls import path
from . import views

urlpatterns = [

    path('employees/', views.employees_all, name='employees'),
    path('employees_detail/<int:id>', views.PersonDetail, name='information'),
    path('add-employees/', views.PersonCreate.as_view(), name='add-person'),
    path('employees/<int:id>/update/', views.PersonUpdate.as_view(), name='information'),
    path('employees/<int:id>/delete/', views.PersonDelete.as_view(), name='information'),

    path('privacy/', views.PrivacyPolicy, name='privacy'),
    path('termsofuse/', views.TermsOfUse, name='termsofuse'),
    path('footer/', views.Footer_all.as_view(), name='footer'),
]







# path('home/', views.home_all, name='home'),