from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic
from .models import Home, Category, Footer

#employees
def employees_all(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    employees = models.Home.objects.filter(category__title__icontains=q)
    category = Category.objects.all()
    context = {
        'employees': employees,
        'category': category,
    }
    return render(request, 'employees.html', context)


#Contacts



#Add-person
class PersonCreate(generic.CreateView):
    template_name = 'add_person.html'
    form_class = forms.PersonForm
    queryset = models.Home.objects.all()
    success_url = '/employees/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PersonCreate, self).form_valid(form=form)

#Update
class PersonUpdate(generic.UpdateView):
    template_name = 'update_person.html'
    form_class = forms.PersonForm
    success_url = '/employees/'

    def get_object(self, **kwargs):
        employees_id = self.kwargs.get('id')
        return get_object_or_404(models.Home, id=employees_id)

    def form_valid(self, form):
        return super(PersonUpdate, self).form_valid(form=form)


#Инфо
# class information_all(generic.DetailView):
#     template_name = 'information.html'
#
#     def get_object(self, **kwargs):
#         home_id = self.kwargs.get('id')
#         return get_object_or_404(models.Home, id=home_id)


#Get id
def PersonDetail(request, id):
    employees = Home.objects.get(id=id)
    context={
        "object": employees,
    }
    return render(request, 'information.html', context)


#Удаление
class PersonDelete(generic.DeleteView):
    template_name = 'delete_person.html'
    success_url = '/employees/'

    def get_object(self, **kwargs):
        employees_id = self.kwargs.get('id')
        return get_object_or_404(models.Home, id=employees_id)






class Footer_all(generic.ListView):
    template_name = 'HeaderandFooter.html'

    def get_queryset(self):
        footer1 = models.Footer.objects.all()
        return footer1






    #То что никто не читает
def PrivacyPolicy(request):
    return render(request, 'privacypolicy.html')
def TermsOfUse(request):
    return render(request, 'termsofuse.html')














def LoginPage(request):
    context = {}
    return render(request, 'login_register.html', context)



# class TvShowDeleteView(generic.DeleteView):
#     template_name = 'tvdelete.html'
#     success_url = '/tvshow/'
#
#     def get_object(self, **kwargs):
#         tvshow_id = self.kwargs.get('id')
#         return get_object_or_404(models.TvShow, id=tvshow_id)

#information about the person:




# def add_person(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.HomeForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Successfully added!!!')
#     else:
#         form = forms.HomeForms()
#     return render(request, 'add_person.html', {'form':form})
#create new post from html page





# def prog_lang_view(request):
#     lang = models.ProgLang.objects.all()
#     return render(request, 'index.html', {'lang_object': lang})
#
# def add_prog_lang_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ProgLangForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен')
#     else:
#         form = forms.ProgLangForms()
#     return render(request, 'add_prog_lang.html', {'form': form})













# def home_all(request):
#     home = models.Home.objects.all()
#     return render(request, 'home.html', {'home': home})

# def add_blog_all(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ProgLangForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен')
#     else:
#         form = forms.ProgLangForms()
#     return render(request, 'add_blog_all.html', {'form': form})
# # Create your views here.

# def add_prog_lang_view(request):
#     method = request.method
#     if method= 'Post':
#         form= forms.ProgLangForms(request.POST, request.FILES)
#         if form.is_valid():
#                 form.save()
#                 return HttpResponse('CUNT')
#         else:
#             form = forms.ProgLangForms()
#         return  render(request, 'add_prog_lang', {'form':form})
