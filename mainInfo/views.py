from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic
from .models import PopularTeachers, Contacts, Stats, AboutInai

#the main page
def main_all(request):
    main = PopularTeachers.objects.all()
    contact = Contacts.objects.all()
    stats = Stats.objects.all()
    aboutInai = AboutInai.objects.all()
    context = {
        'main': main,
        'contact': contact,
        'stats': stats,
        'aboutInai':aboutInai
    }
    return render(request, 'main.html',context)

#About Inai
class AboutInaiUpdate(generic.UpdateView):
    template_name = 'update_aboutInai.html'
    form_class = forms.AboutInaiForm
    success_url = '/main/'
    
    def get_object(self, **kwargs):
        aboutInai_id = self.kwargs.get('id')
        return get_object_or_404(models.AboutInai, id=aboutInai_id)
    def form_valid(self, form):
        return super(AboutInaiUpdate, self).form_valid(form=form)


# Popular teachers:
class PopularCreate(generic.CreateView):
    template_name = 'add_popular.html'
    form_class = forms.PopularForm
    queryset = models.PopularTeachers.objects.all()
    success_url = '/main/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PopularCreate, self).form_valid(form=form)


class PopularUpdate(generic.UpdateView):
    template_name = 'update_popular.html'
    form_class = forms.PopularForm
    success_url = '/main/'

    def get_object(self, **kwargs):
        main_id = self.kwargs.get('id')
        return get_object_or_404(models.PopularTeachers, id=main_id)

    def form_valid(self, form):
        return super(PopularUpdate, self).form_valid(form=form)


class PopularDelete(generic.DeleteView):
    template_name = 'delete_popular.html'
    success_url = '/main/'

    def get_object(self, **kwargs):
        main_id = self.kwargs.get('id')
        return get_object_or_404(models.PopularTeachers, id=main_id)





#CRUD for the contacts
class ContactCreate(generic.CreateView):
    template_name = 'add-contact.html'
    form_class = forms.ContactsForm
    queryset = models.Contacts.objects.all()
    success_url = "/main/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ContactCreate, self).form_valid(form=form)


class ContactDelete(generic.DeleteView):
    template_name = 'delete_contact.html'
    success_url = '/main/'

    def get_object(self, **kwargs):
        contact_id = self.kwargs.get('id')
        return get_object_or_404(models.Contacts, id=contact_id)

class ContactUpdate(generic.UpdateView):
    template_name = 'update_contact.html'
    form_class = forms.ContactsForm
    success_url = '/main/'

    def get_object(self, **kwargs):
        contact_id = self.kwargs.get('id')
        return get_object_or_404(models.Contacts, id=contact_id)

    def form_valid(self, form):
        return super(ContactUpdate, self).form_valid(form=form)



#Update the stats
class StatsUpdate(generic.UpdateView):
    template_name = 'update_stats.html'
    form_class = forms.StatsForm
    success_url = '/main/'

    def get_object(self, **kwargs):
        stats_id = self.kwargs.get('id')
        return get_object_or_404(models.Stats, id=stats_id)

    def form_valid(self, form):
        return super(StatsUpdate, self).form_valid(form=form)









    