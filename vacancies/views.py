from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.views import generic
from .models import Vacancy

# Create your views here.
def vacancy(request):
    vacancy = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancy':vacancy})

#Сraete a vacancy
class VacancyCreate(generic.CreateView):
    template_name = 'vacancycreate.html'
    form_class = forms.VacancyForm
    queryset = models.Vacancy.objects.all()
    success_url = "/vacancy/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(VacancyCreate, self).form_valid(form=form)

#Delete a vacancy
class VacancyDelete(generic.DeleteView):
    template_name = 'vacancydelete.html'
    success_url = '/vacancy/'

    def get_object(self, **kwargs):
        vacancy_id = self.kwargs.get('id')
        return get_object_or_404(models.Vacancy, id=vacancy_id)



#Up a vacancy
class VacancyUpdate(generic.UpdateView):
    template_name = 'update_vacancy.html'
    form_class = forms.VacancyForm
    success_url = '/vacancy/'

    def get_object(self, **kwargs):
        vacancy_id = self.kwargs.get('id')
        return get_object_or_404(models.Vacancy, id=vacancy_id)

    def form_valid(self, form):
        return super(VacancyUpdate, self).form_valid(form=form)















