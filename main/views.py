from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import cloud
from django.views.generic import DetailView
from django.http import Http404
from .forms import *
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def index(request):
    all_clouds = cloud.objects.all()
    your_id = ''
    error = ''
   # your_id = request.GET.get('ident', None)



    if request.method == 'POST':
        form = IdentForm(request.POST)
        if form.is_valid():
            ident = form.cleaned_data['ident']
            try:
                obj = cloud.objects.get(ident=ident)
                return render(request, 'detail_cloud.html', {'cloud': obj})
            except cloud.DoesNotExist:
                error = 'Page does not exist'
                return render(request, 'error.html', {'error': error})
            except cloud.MultipleObjectsReturned:
                error = 'Multiple objects returned'
                return render(request, 'error.html', {'error': error})
                #raise Http404("Page does not exist")
    else:
        form = IdentForm()
    return render(request, 'index.html', {'all_clouds': all_clouds, 'form': form, 'your_id': your_id})
def about(request):
    return render(request, 'about.html')
def success_created(request):
    your_id = ''
    your_id = request.GET.get('ident', None)
    return render(request,"success_created.html", {'your_id': your_id})
def create(request):
    error = ''
    if request.method == 'POST':
        form = CloudForm(request.POST, request.FILES)
        #form.initial['ident'] = 100000

        if form.is_valid() == True:
            has_file_uploaded = any(request.FILES.values())
            if (has_file_uploaded):
                clearData()
            instance = form.save()
            redirect_url = f'/success_created/?ident={instance.ident}'
            return redirect(redirect_url)
           # return redirect('home')
        else:
            error = form.errors

    form = CloudForm()

    return render(request, 'create.html', {'form': form, 'error': error})
def clearData():
    current_datetime = timezone.now()
    seven_days_ago = current_datetime - timedelta(days=7)  # Исправлено с 'сurrent_datetime' на 'current_datetime'

    # Получаем все записи, у которых поле 'date' меньше или равно семи дням назад
    old_records = cloud.objects.filter(date__lte=seven_days_ago)

    # Удаляем найденные записи
    old_records.delete()
def error(request):
    return render(request, 'error.html')
class Detail_Cloud(DetailView):
    model = cloud
    template_name = 'detail_cloud.html'
    context_object_name = 'cloud'

    def get_object(self, queryset=None):
        ident = self.kwargs['pk']  # Получаем значение pk из URL
        try:
            return self.model.objects.get(ident=ident)
        except self.model.DoesNotExist:
            raise Http404("Page does not exist")  # Отобразить страницу 404
